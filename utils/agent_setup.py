from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI


def create_agent(df, df2):
    """Creates an agent for processing dataframes.

    This function initializes a pandas dataframe agent that utilizes the
    ChatOpenAI model to provide responses based on the provided dataframes.

    Args:
        df (DataFrame): The first dataframe containing service occupancy data.
        df2 (DataFrame): The second dataframe containing service information.

    Returns:
        Agent: A pandas dataframe agent configured with the provided dataframes.
    """
    custom_prefix = (
        "You have data on Toronto and Memphis. "
        "Dataset df contains fields related to service occupancy, and df2 contains fields related to service information. "
        "The dataframe output should be human-readable and exclude unnecessary details."
    )
    custom_suffix = """
        You are a compassionate and approachable city service chatbot focused on helping users find public services in Toronto and Memphis.
        Always communicate in a warm and supportive manner, ensuring users feel heard and understood.
        Responses should be formatted clearly for a plain text message, without any code or markdown.
    """

    return create_pandas_dataframe_agent(
        ChatOpenAI(model="placeholder_model_name", temperature=0),
        [df, df2],
        suffix=custom_suffix,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        allow_dangerous_code=True,
    )
