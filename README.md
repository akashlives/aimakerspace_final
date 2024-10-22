# AI MakerSpace Final Demo: City Services SMS Assistant

This Flask application serves as an AI-powered SMS assistant to help users navigate city services in Toronto and Memphis.

## Features

-   Receive and respond to SMS messages using Twilio
-   Process user queries using a LangChain-based AI agent
-   Maintain conversation history for each user
-   Load and utilize data from external sources (DataFrames)
-   Send SMS messages programmatically

## Technologies Used

-   Python 3.12
-   Flask
-   LangChain
-   OpenAI GPT
-   Twilio
-   Pandas
-   Poetry (for dependency management)

## Code Structure

-   `app.py`: Main Flask application file
-   `utils/`:
    -   `data_loader.py`: Functions to load DataFrames
    -   `agent_setup.py`: Setup for the LangChain AI agent
    -   `memory_manager.py`: Manage user conversation history
    -   `twilio_client.py`: Twilio client setup and SMS sending function
    -   `config.py`: Configuration and environment variables

## API Endpoints

-   `/`: Index route, confirms the app is running
-   `/check-df`: Check if the DataFrame is loaded correctly
-   `/send-sms`: POST endpoint to send SMS messages
-   `/sms`: POST endpoint to receive and process incoming SMS messages

## Error Handling

The application includes basic error handling for:

-   Missing SMS parameters
-   Empty DataFrames
-   Exceptions during message processing

## Data Management

-   The application uses two DataFrames loaded from parquet files
-   User conversation history is managed with a time-based reset mechanism

## AI Agent

-   Utilizes LangChain and OpenAI's GPT model
-   Customized to provide friendly and informative responses about city services

## Future Improvements

-   Implement user authentication for secure access to sensitive information
-   Add more comprehensive error logging and monitoring
-   Expand the dataset to cover more cities and services
-   Implement multi-language support for diverse user bases

## License

This project is licensed under the Apache License - see the LICENSE file for details.
