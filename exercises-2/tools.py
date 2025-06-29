# Weather and search tools for REACT agent
from langchain_community.tools.tavily_search import TavilySearchResults

# TODO: Implement weather search function
def get_weather_with_tavily(city: str) -> str:
    """
    Get current weather for a city using Tavily search.
    
    Steps:
    1. Initialize TavilySearchResults with max_results=2
    2. Create a weather query for the city
    3. Invoke the search tool
    4. Format and return the results
    
    Args:
        city: Name of the city to get weather for
        
    Returns:
        Formatted weather information string
    """
    # Your code here:
    return ""  # Replace with proper implementation

# TODO: Implement general search function
def search_additional_info(query: str) -> str:
    """
    Search for additional information using Tavily.
    This tool can be used when the agent decides it needs more context.
    
    Args:
        query: Search query string
        
    Returns:
        Search results as formatted string
    """
    # Your code here:
    return ""  # Replace with proper implementation 