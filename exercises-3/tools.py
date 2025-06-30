# Search tools for Travel Planning Supervisor Agent
from typing import Optional
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

@tool
def search_weather_info(destination: str, travel_dates: Optional[str] = None) -> str:
    """
    Search for weather information for a specific destination and dates.
    Reuses weather search functionality from Exercise 2.
    
    Args:
        destination: Travel destination city/country
        travel_dates: When the user plans to travel (optional)
        
    Returns:
        Weather forecast and recommendations
        
    TODO: Implement weather search using Tavily
    - Create appropriate search query including destination and dates
    - Use TavilySearchResults to get weather data
    - Format results with temperature, conditions, and packing advice
    - Return formatted weather information string
    """
    # TODO: Initialize Tavily search tool
    
    # TODO: Create weather-specific search query
    
    # TODO: Execute search and process results
    
    # TODO: Format and return weather information
    return "TODO: Implement weather search"

@tool  
def search_flights(origin: str, destination: str, travel_dates: Optional[str] = None, budget: Optional[str] = None) -> str:
    """
    Search for flight information between origin and destination.
    
    Args:
        origin: Departure location
        destination: Arrival destination  
        travel_dates: Travel dates if specified
        budget: Budget constraints if any
        
    Returns:
        Flight options, prices, and booking recommendations
        
    TODO: Implement flight search using Tavily
    - Create search query for flights between origin and destination
    - Include dates and budget constraints in search
    - Look for airline options, prices, duration
    - Format results with flight details and recommendations
    """
    # TODO: Initialize Tavily search tool
    
    # TODO: Build flight search query with all parameters
    
    # TODO: Execute search and extract flight information
    
    # TODO: Format flight options and return results
    return "TODO: Implement flight search"

@tool
def search_accommodation(destination: str, travel_dates: Optional[str] = None, budget: Optional[str] = None) -> str:
    """
    Search for accommodation options in the destination.
    
    Args:
        destination: Where to find accommodation
        travel_dates: Check-in/check-out dates if available
        budget: Budget range for accommodation
        
    Returns:
        Hotel, hostel, and lodging options with prices and amenities
        
    TODO: Implement accommodation search using Tavily
    - Create search query for hotels and lodging in destination
    - Include date availability and budget constraints
    - Look for different types of accommodation (hotels, hostels, apartments)
    - Format results with prices, amenities, and recommendations
    """
    # TODO: Initialize Tavily search tool
    
    # TODO: Create accommodation search query
    
    # TODO: Search for different types of lodging options
    
    # TODO: Format accommodation results with details
    return "TODO: Implement accommodation search"

@tool
def search_activities(destination: str, travel_dates: Optional[str] = None, interests: Optional[str] = None) -> str:
    """
    Search for activities, attractions, and things to do at destination.
    
    Args:
        destination: Where to find activities
        travel_dates: When visiting (for seasonal activities)
        interests: User preferences for activity types
        
    Returns:
        Local attractions, restaurants, entertainment, and experiences
        
    TODO: Implement activity search using Tavily
    - Create search query for attractions and activities
    - Include seasonal considerations based on travel dates
    - Look for restaurants, museums, tours, entertainment
    - Consider user interests if provided
    - Format results with activity suggestions and details
    """
    # TODO: Initialize Tavily search tool
    
    # TODO: Build activity search query
    
    # TODO: Search for attractions and experiences
    
    # TODO: Format activity recommendations
    return "TODO: Implement activity search"

@tool
def search_budget_info(destination: str, travel_dates: Optional[str] = None, trip_type: Optional[str] = None) -> str:
    """
    Search for budget and cost information for the destination.
    
    Args:
        destination: Where to research costs
        travel_dates: When traveling (affects seasonal pricing)
        trip_type: Type of trip (business, leisure, backpacking)
        
    Returns:
        Cost estimates, budget breakdowns, and money-saving tips
        
    TODO: Implement budget research using Tavily
    - Create search query for cost of living and travel expenses
    - Look for daily budget estimates, typical costs
    - Find money-saving tips and budget travel advice
    - Consider seasonal price variations
    - Format results with budget breakdowns and recommendations
    """
    # TODO: Initialize Tavily search tool
    
    # TODO: Create budget research query
    
    # TODO: Search for cost information and budget tips
    
    # TODO: Format budget information and recommendations
    return "TODO: Implement budget search"

# List of all available tools for the supervisor to use
tools = [
    search_weather_info,
    search_flights, 
    search_accommodation,
    search_activities,
    search_budget_info
] 