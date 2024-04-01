import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from get_website_data import get_website_results
from get_table_data import get_table_results

# Load environment variables
load_dotenv()

# Get the OPENAI_API_KEY from environment variable
key = os.getenv("OPENAI_API_KEY")

# Initialize the ChatOpenAI object
chat = ChatOpenAI(
    openai_api_key=key,
    model_name="gpt-3.5-turbo",
    temperature=0.2
)


def final_result(query):
    """
    Generates a final result based on table data and website data for the given query.
    """
    # Get data from table
    get_table_data = get_table_results(query)
    # Get data from website
    get_website_data = get_website_results(query)

    # Prepare prompt for the ChatOpenAI
    prompt = (
        f"The Question from user is {query}. "
        f"The answer from table information is {get_table_data}, "
        f"The answer from website information is {get_website_data}. "
        "Carefully read the question and the results from table and website and provide answer to the user."
    )

    # Generate response using ChatOpenAI
    response = chat.predict(prompt)

    return response
