import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent

# Load environment variables
load_dotenv()

# Retrieve the OPENAI_API_KEY from environment variable
key = os.environ.get("OPENAI_API_KEY")


def get_table_results(query):
    """
    Generates results based on a query by invoking an agent that operates on CSV data.
    """
    # Initialize the ChatOpenAI object with specified parameters
    chat = ChatOpenAI(
        openai_api_key=key,
        model_name="gpt-3.5-turbo",
        temperature=0.2
    )

    # Create a CSV agent using the chat model and specifying the CSV file
    agent = create_csv_agent(chat, "universities_data.csv", verbose=True)

    # Invoke the agent with the provided query and return the results
    return agent.invoke(query)
