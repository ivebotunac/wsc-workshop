# Search tools for Travel Planning Supervisor Agent
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

@tool
def search_weather_info(user_query: str) -> str:
    """
    Search for weather information based on user's travel request.
    
    Args:
        user_query: User's complete travel request
        
    Returns:
        Weather forecast and recommendations
    """
    search = TavilySearchResults(max_results=3)
    query = f"{user_query} - Search for weather forecast climate packing recommendations"
    results = search.run(query)
    return str(results)

@tool  
def search_flights(user_query: str) -> str:
    """
    Search for flight information based on user's travel request.
    
    Args:
        user_query: User's complete travel request
        
    Returns:
        Flight options, prices, and booking recommendations
    """
    search = TavilySearchResults(max_results=3)
    query = f"{user_query} - Search for flights airline prices booking"
    results = search.run(query)
    return str(results)

@tool
def search_accommodation(user_query: str) -> str:
    """
    Search for accommodation options based on user's travel request.
    
    Args:
        user_query: User's complete travel request
        
    Returns:
        Hotel, hostel, and lodging options with prices and amenities
    """
    search = TavilySearchResults(max_results=3)
    query = f"{user_query} - Search for hotels accommodation booking prices reviews"
    results = search.run(query)
    return str(results)

@tool
def search_activities(user_query: str) -> str:
    """
    Search for activities and attractions based on user's travel request.
    
    Args:
        user_query: User's complete travel request
        
    Returns:
        Local attractions, restaurants, entertainment, and experiences
    """
    search = TavilySearchResults(max_results=3)
    query = f"{user_query} - Search for things to do attractions restaurants tours"
    results = search.run(query)
    return str(results)

@tool
def search_budget_info(user_query: str) -> str:
    """
    Search for budget and cost information based on user's travel request.
    
    Args:p
        user_query: User's complete travel request
        
    Returns:
        Cost estimates, budget breakdowns, and money-saving tips
    """
    search = TavilySearchResults(max_results=3)
    query = f"{user_query} - Search for travel budget cost daily expenses money saving tips"
    results = search.run(query)
    return str(results)

# List of all available tools
tools = [
    search_weather_info,
    search_flights, 
    search_accommodation,
    search_activities,
    search_budget_info
] 