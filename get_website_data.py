from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper

# Load environment variables
load_dotenv()


def get_website_results(query):
    """
    Performs a Google search for the given query and prints the results.
    """
    # Initialize the GoogleSerperAPIWrapper object
    search = GoogleSerperAPIWrapper()

    # Run the search with the provided query
    result = search.run(query)

    # Print the search results
    print(result)
