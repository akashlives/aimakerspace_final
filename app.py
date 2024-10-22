from flask import Flask, reques
from langchain_core.messages import HumanMessage, AIMessage

from utils.data_loader import load_dataframes
from utils.agent_setup import create_agent
from utils.memory_manager import get_user_memory, update_user_memory
from utils.twilio_client import send_sms, create_twiml_response

app = Flask(__name__)

df, df2 = load_dataframes()

agent = create_agent(df, df2)


@app.route("/check-df")
def check_df():
    """
    Check if the DataFrame is loaded and return its status.

    Returns:
        str: A message indicating whether the DataFrame is empty or the number of rows loaded.
    """
    if df.empty:
        return "DataFrame is empty."
    else:
        return f"DataFrame loaded with {len(df)} rows."


@app.route("/")
def index():
    """
    Provide a simple index route for the Twilio Flask App.

    Returns:
        str: A message indicating that the Twilio Flask App is running.
    """
    return "Twilio Flask App is running."


@app.route("/send-sms", methods=["POST"])
def send_sms_route():
    """
    Handle POST requests to send SMS messages.

    Returns:
        tuple: A tuple containing the response from send_sms function and an HTTP status code.

    Raises:
        400: If 'To' or 'Body' parameters are missing from the request.
    """
    body = request.form.get("Body")
    to = request.form.get("To")

    if not to or not body:
        return "Missing 'To' or 'Body' parameter.", 400

    return send_sms(body, to)


@app.route("/sms", methods=["POST"])
def sms_reply():
    """
    Handle incoming SMS messages and generate responses using the AI agent.

    Returns:
        str: The TwiML response as a string.

    Note:
        This function processes incoming messages, interacts with the AI agent,
        and manages user conversation history.
    """
    incoming_msg = request.form.get("Body")
    from_number = request.form.get("From")

    if not incoming_msg:
        response_text = "Sorry, I didn't receive any message. Please try again."
    else:
        try:
            print(f"Processing message from {from_number}: {incoming_msg}")

            if df.empty:
                response_text = "Data is not available. Please check the data source."
            else:
                user_conversation_history = get_user_memory(from_number)
                user_conversation_history.append(HumanMessage(content=incoming_msg))

                response = agent.invoke({"input": user_conversation_history})

                if isinstance(response, dict) and "output" in response:
                    response_text = response["output"]
                    update_user_memory(from_number, AIMessage(content=response_text))
                else:
                    response_text = "I'm sorry, I couldn't process that request."

        except Exception as e:
            response_text = f"An error occurred: {str(e)}"
            print(f"Error processing message from {from_number}: {str(e)}")

    print(f"Responded to {from_number} with: {response_text}")
    return create_twiml_response(response_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000, debug=True)
