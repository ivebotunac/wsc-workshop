# Weather tool using Tavily search API
from langchain_community.tools.tavily_search import TavilySearchResults

def get_weather_with_tavily(city: str) -> str:
    """Get current weather for a city using Tavily search"""
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