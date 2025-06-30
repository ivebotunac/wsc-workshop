# Specialized travel planning agents for supervisor system
from typing import Optional
from langchain_core.messages import HumanMessage, AIMessage
from .state import TravelPlanState, AgentResponse
from .tools import search_weather_info, search_flights, search_accommodation, search_activities, search_budget_info

def weather_agent(state: TravelPlanState) -> dict:
    """
    Weather Agent - Analyzes weather forecasts and provides packing recommendations.
    Reuses weather functionality from Exercise 2.
    
    Args:
        state: Current travel planning state
        
    Returns:
        Updated state with weather agent response
        
    TODO: Implement weather agent logic
    - Extract destination and travel dates from state
    - Use search_weather_info tool to get weather data
    - Analyze weather patterns and seasonal considerations
    - Provide packing recommendations based on weather
    - Create AgentResponse with weather findings
    - Add response to state.agent_responses
    - Add a summary message to state.messages
    """
    # TODO: Extract destination from state
    
    # TODO: Extract travel dates if available
    
    # TODO: Call search_weather_info tool
    
    # TODO: Analyze weather results and create recommendations
    
    # TODO: Create AgentResponse with weather data
    
    # TODO: Add agent response to state
    
    # TODO: Add summary message to conversation
    
    return {"messages": [AIMessage(content="TODO: Implement weather agent")]}

def flight_agent(state: TravelPlanState) -> dict:
    """
    Flight Agent - Searches for flight options and provides booking recommendations.
    
    Args:
        state: Current travel planning state
        
    Returns:
        Updated state with flight agent response
        
    TODO: Implement flight agent logic
    - Extract destination and travel dates from state
    - Determine origin location (ask user or use default)
    - Use search_flights tool to find flight options
    - Compare airlines, prices, and routes
    - Provide booking recommendations and tips
    - Create AgentResponse with flight data
    - Add response to state.agent_responses
    """
    # TODO: Extract destination and dates from state
    
    # TODO: Determine origin location for flights
    
    # TODO: Call search_flights tool
    
    # TODO: Analyze flight options and prices
    
    # TODO: Create AgentResponse with flight recommendations
    
    # TODO: Update state with flight response
    
    return {"messages": [AIMessage(content="TODO: Implement flight agent")]}

def accommodation_agent(state: TravelPlanState) -> dict:
    """
    Accommodation Agent - Finds lodging options and compares amenities.
    
    Args:
        state: Current travel planning state
        
    Returns:
        Updated state with accommodation agent response
        
    TODO: Implement accommodation agent logic
    - Extract destination, dates, and budget from state
    - Use search_accommodation tool to find lodging options
    - Compare hotels, hostels, apartments, and other options
    - Consider amenities, location, and price
    - Provide accommodation recommendations
    - Create AgentResponse with lodging data
    - Add response to state.agent_responses
    """
    # TODO: Extract destination, dates, and budget constraints
    
    # TODO: Call search_accommodation tool
    
    # TODO: Analyze accommodation options
    
    # TODO: Compare prices and amenities
    
    # TODO: Create AgentResponse with accommodation recommendations
    
    # TODO: Update state with accommodation response
    
    return {"messages": [AIMessage(content="TODO: Implement accommodation agent")]}

def activities_agent(state: TravelPlanState) -> dict:
    """
    Activities Agent - Discovers local attractions and creates itinerary suggestions.
    
    Args:
        state: Current travel planning state
        
    Returns:
        Updated state with activities agent response
        
    TODO: Implement activities agent logic
    - Extract destination and travel dates from state
    - Use search_activities tool to find attractions
    - Consider seasonal activities and weather constraints
    - Find restaurants, museums, tours, and entertainment
    - Create suggested daily itineraries
    - Consider travel duration from accommodation search
    - Create AgentResponse with activity recommendations
    - Add response to state.agent_responses
    """
    # TODO: Extract destination and dates from state
    
    # TODO: Call search_activities tool
    
    # TODO: Consider weather data for outdoor activities
    
    # TODO: Create itinerary suggestions
    
    # TODO: Create AgentResponse with activity recommendations
    
    # TODO: Update state with activities response
    
    return {"messages": [AIMessage(content="TODO: Implement activities agent")]}

def budget_agent(state: TravelPlanState) -> dict:
    """
    Budget Agent - Calculates trip costs and provides budget recommendations.
    
    Args:
        state: Current travel planning state
        
    Returns:
        Updated state with budget agent response
        
    TODO: Implement budget agent logic
    - Extract destination and travel dates from state
    - Use search_budget_info tool to get cost information
    - Analyze responses from other agents for price data
    - Calculate total trip cost estimates
    - Provide budget breakdowns (flights, accommodation, food, activities)
    - Suggest money-saving tips and alternatives
    - Create AgentResponse with budget analysis
    - Add response to state.agent_responses
    """
    # TODO: Extract destination and travel parameters
    
    # TODO: Call search_budget_info tool
    
    # TODO: Collect cost data from other agent responses
    
    # TODO: Calculate total trip cost estimates
    
    # TODO: Create budget breakdown and recommendations
    
    # TODO: Create AgentResponse with budget analysis
    
    # TODO: Update state with budget response
    
    return {"messages": [AIMessage(content="TODO: Implement budget agent")]}

# Agent registry for supervisor routing
AVAILABLE_AGENTS = {
    "weather": weather_agent,
    "flight": flight_agent, 
    "accommodation": accommodation_agent,
    "activities": activities_agent,
    "budget": budget_agent
} 