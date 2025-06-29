# Weather and search tools for REACT agent
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

@tool
def get_weather_with_tavily(city: str) -> str:
    """
    Get current weather for a city using Tavily search.
    
    Args:
        city: Name of the city to get weather for
        
    Returns:
        Formatted weather information string
    """
    # Initialize search tool with max 2 results
    search_tool = TavilySearchResults(max_results=2)
    query = f"What is the current weather in {city} and today's temperature?"
    results = search_tool.invoke(query)
    
    # Combine search results into weather info
    if results:
        weather_info = " ".join([result['content'][:150] for result in results[:2]])
        return f"Weather in {city}: {weather_info}"
    else:
        return f"Weather in {city}: No current weather data available"

@tool 
def search_additional_info(query: str) -> str:
    """
    Search for additional information using Tavily.
    This tool can be used when the agent decides it needs more context.
    
    Args:
        query: Search query string
        
    Returns:
        Search results as formatted string
    """
    # Initialize search tool with max 3 results for broader search
    search_tool = TavilySearchResults(max_results=3)
    results = search_tool.invoke(query)
    
    if results:
        search_info = " ".join([result['content'][:200] for result in results[:3]])
        return f"Search results for '{query}': {search_info}"
    else:
        return f"No search results found for: {query}"

# List of all available tools
tools = [get_weather_with_tavily, search_additional_info] 