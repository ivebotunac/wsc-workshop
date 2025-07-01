# Supervisor agent for coordinating travel planning specialists
from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from state import TravelPlanState
from agents import AVAILABLE_AGENTS

def create_supervisor_chain():
    """Creates supervisor LLM chain for routing decisions"""
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a Travel Planning Supervisor who coordinates a team of specialized agents.

Your team consists of:
- weather: Analyzes weather and provides packing recommendations
- flight: Searches flights and booking options
- accommodation: Finds hotels and accommodation  
- activities: Discovers attractions and creates itineraries
- budget: Calculates costs and provides budget analysis

When a user sends a travel planning request, analyze what they need and decide which agent should work next.

Respond ONLY with the agent name (weather, flight, accommodation, activities, or budget) or "FINISH" if planning is complete.

Logic: Run all agents one by one to achieve complete travel analysis."""),
        ("human", "{input}")
    ])
    
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
    return prompt | llm

def supervisor_node(state: TravelPlanState) -> dict:
    """Supervisor node that analyzes state and routes to agents"""
    
    # Check which agents have already worked
    completed_agents = set()
    for msg in state["messages"]:
        if isinstance(msg, AIMessage) and isinstance(msg.content, str):
            if "Weather Agent:" in msg.content:
                completed_agents.add("weather")
            elif "Flight Agent:" in msg.content:
                completed_agents.add("flight")
            elif "Accommodation Agent:" in msg.content:
                completed_agents.add("accommodation")
            elif "Activities Agent:" in msg.content:
                completed_agents.add("activities")
            elif "Budget Agent:" in msg.content:
                completed_agents.add("budget")
    
    # Supervisor logic - run agents one by one
    available_agents = ["weather", "flight", "accommodation", "activities", "budget"]
    
    for agent in available_agents:
        if agent not in completed_agents:
            return {"next_agent": agent}
    
    # All agents have finished
    return {"next_agent": "FINISH"}

def should_continue(state: TravelPlanState) -> Literal["continue", "end"]:
    """Decides whether workflow should continue"""
    next_agent = state.get("next_agent")
    
    if next_agent == "FINISH":
        return "end"
    else:
        return "continue"

def route_to_agent(state: TravelPlanState) -> str:
    """Routes workflow to appropriate agent"""
    next_agent = state.get("next_agent")
    
    if next_agent in AVAILABLE_AGENTS:
        return next_agent
    else:
        return "weather"  # Default

def final_coordinator(state: TravelPlanState) -> dict:
    """Final coordinator that combines all agent responses"""
    
    # Combine all agent responses
    agent_summaries = []
    for msg in state["messages"]:
        if isinstance(msg, AIMessage) and isinstance(msg.content, str):
            if any(agent in msg.content for agent in ["Weather Agent:", "Flight Agent:", "Accommodation Agent:", "Activities Agent:", "Budget Agent:"]):
                agent_summaries.append(msg.content)
    
    # Pass to LLM to create final travel plan
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)
    
    final_prompt = f"""
    Based on all the research from specialized agents:
    
    {chr(10).join(agent_summaries)}
    
    Please create a short travel plan summary that combines all this information into a cohesive, actionable travel guide.
    Include an executive summary and highlight the key recommendations from each area.
    """
    
    final_plan = llm.invoke(final_prompt).content
    
    return {
        "messages": [AIMessage(content=f"🎯 COMPREHENSIVE TRAVEL PLAN:\n\n{final_plan}")],
        "planning_complete": True
    } 