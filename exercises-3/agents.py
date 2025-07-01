# Specialized travel planning agents for supervisor system
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from state import TravelPlanState
from tools import search_weather_info, search_flights, search_accommodation, search_activities, search_budget_info

def get_user_query(state: TravelPlanState) -> str:
    """Extracts user query from messages"""
    for msg in state["messages"]:
        if isinstance(msg, HumanMessage) and isinstance(msg.content, str):
            return msg.content
    return ""

def weather_agent(state: TravelPlanState) -> dict:
    """Weather Agent - calls search and passes to LLM"""
    user_query = get_user_query(state)
    
    # Call search tool
    search_results = search_weather_info.invoke(user_query)
    
    # Pass to LLM for analysis
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)
    prompt = f"""
    User request: {user_query}
    
    Weather search results: {search_results}
    
    Based on this information, provide a short and helpful weather analysis and recommendations for the trip.
    Include packing suggestions and weather-related travel tips.
    """
    
    analysis = llm.invoke(prompt).content
    
    return {"messages": [AIMessage(content=f"🌤️ Weather Agent:\n{analysis}")]}

def flight_agent(state: TravelPlanState) -> dict:
    """Flight Agent - calls search and passes to LLM"""
    user_query = get_user_query(state)
    
    # Call search tool
    search_results = search_flights.invoke(user_query)
    
    # Pass to LLM for analysis
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)
    prompt = f"""
    User request: {user_query}
    
    Flight search results: {search_results}
    
    Based on this information, provide a short and helpful flight recommendations and booking advice.
    Include price comparisons and travel tips.
    """
    
    analysis = llm.invoke(prompt).content
    
    return {"messages": [AIMessage(content=f"✈️ Flight Agent:\n{analysis}")]}

def accommodation_agent(state: TravelPlanState) -> dict:
    """Accommodation Agent - calls search and passes to LLM"""
    user_query = get_user_query(state)
    
    # Call search tool
    search_results = search_accommodation.invoke(user_query)
    
    # Pass to LLM for analysis
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)
    prompt = f"""
    User request: {user_query}
    
    Accommodation search results: {search_results}
    
    Based on this information, provide a short and helpful accommodation recommendations.
    Include comparisons of options, amenities, and booking advice.
    """
    
    analysis = llm.invoke(prompt).content
    
    return {"messages": [AIMessage(content=f"🏨 Accommodation Agent:\n{analysis}")]}

def activities_agent(state: TravelPlanState) -> dict:
    """Activities Agent - calls search and passes to LLM"""
    user_query = get_user_query(state)
    
    # Call search tool
    search_results = search_activities.invoke(user_query)
    
    # Pass to LLM for analysis
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)
    prompt = f"""
    User request: {user_query}
    
    Activities search results: {search_results}
    
    Based on this information, provide a short and helpful activity and attraction recommendations.
    Include itinerary suggestions and local experiences.
    """
    
    analysis = llm.invoke(prompt).content
    
    return {"messages": [AIMessage(content=f"🎯 Activities Agent:\n{analysis}")]}

def budget_agent(state: TravelPlanState) -> dict:
    """Budget Agent - calls search and passes to LLM"""
    user_query = get_user_query(state)
    
    # Call search tool
    search_results = search_budget_info.invoke(user_query)
    
    # Pass to LLM for analysis
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)
    prompt = f"""
    User request: {user_query}
    
    Budget search results: {search_results}
    
    Based on this information, provide a short and helpful budget analysis and cost recommendations.
    Include expense breakdowns and money-saving tips.
    """
    
    analysis = llm.invoke(prompt).content
    
    return {"messages": [AIMessage(content=f"💰 Budget Agent:\n{analysis}")]}

# Agent registry for supervisor routing
AVAILABLE_AGENTS = {
    "weather": weather_agent,
    "flight": flight_agent, 
    "accommodation": accommodation_agent,
    "activities": activities_agent,
    "budget": budget_agent
} 