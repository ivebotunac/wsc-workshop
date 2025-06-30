# Supervisor agent for coordinating travel planning specialists
from typing import Literal
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from .state import TravelPlanState
from .agents import AVAILABLE_AGENTS

# Supervisor system prompt that defines routing behavior
SUPERVISOR_PROMPT = """
You are a Travel Planning Supervisor that coordinates a team of specialized agents to create comprehensive travel plans.

Your team consists of:
- weather: Analyzes weather forecasts and packing recommendations
- flight: Searches flights and booking options
- accommodation: Finds hotels and lodging options  
- activities: Discovers attractions and creates itineraries
- budget: Calculates costs and provides budget analysis

Your job is to:
1. Analyze user travel requests
2. Determine which agents need to gather information
3. Route tasks to appropriate agents in logical order
4. Coordinate results from all agents
5. Provide final comprehensive travel recommendations

Given the user's request and current conversation, decide which agent should work next.
Respond with just the agent name or "FINISH" if planning is complete.

Available agents: {agents}
"""

def create_supervisor_chain():
    """
    Create the supervisor LLM chain for routing decisions.
    
    TODO: Implement supervisor chain creation
    - Create ChatPromptTemplate with supervisor prompt
    - Include MessagesPlaceholder for conversation history
    - Initialize ChatOpenAI model 
    - Create and return the complete chain
    
    Returns:
        Configured supervisor chain for routing decisions
    """
    # TODO: Create prompt template with supervisor instructions
    
    # TODO: Initialize ChatOpenAI model for supervisor
    
    # TODO: Create the supervisor chain
    
    # TODO: Return configured chain
    pass

def supervisor_node(state: TravelPlanState) -> dict:
    """
    Supervisor node that analyzes current state and routes to appropriate agents.
    
    Args:
        state: Current travel planning state
        
    Returns:
        Updated state with next_agent routing decision
        
    TODO: Implement supervisor routing logic
    - Get supervisor chain from create_supervisor_chain()
    - Analyze current state and conversation history
    - Determine which agent should work next based on:
        * User's original request
        * What information has already been gathered
        * What's still missing for complete travel plan
    - Update state.next_agent with routing decision
    - Add supervisor message to conversation if needed
    """
    # TODO: Get supervisor chain
    
    # TODO: Analyze current state and determine next agent
    
    # TODO: Invoke supervisor chain to get routing decision
    
    # TODO: Update state with next_agent decision
    
    # TODO: Add supervisor message to conversation
    
    return {"next_agent": "weather"}  # Placeholder

def should_continue(state: TravelPlanState) -> Literal["continue", "end"]:
    """
    Conditional edge function that determines if supervisor workflow should continue.
    
    Args:
        state: Current travel planning state
        
    Returns:
        "continue" if more agents need to work, "end" if planning is complete
        
    TODO: Implement continuation logic
    - Check if supervisor decided "FINISH" 
    - Check if all necessary agents have provided responses
    - Check if planning_complete flag is set
    - Return "end" if planning is done, "continue" otherwise
    """
    # TODO: Check if supervisor decided to finish
    
    # TODO: Check completion status
    
    # TODO: Return appropriate routing decision
    
    return "continue"  # Placeholder

def route_to_agent(state: TravelPlanState) -> str:
    """
    Router function that directs workflow to the appropriate agent.
    
    Args:
        state: Current travel planning state
        
    Returns:
        Name of the next agent to execute
        
    TODO: Implement agent routing
    - Read state.next_agent to determine routing
    - Validate agent exists in AVAILABLE_AGENTS
    - Return agent name for workflow routing
    - Handle edge cases (invalid agent names, etc.)
    """
    # TODO: Get next agent from state
    
    # TODO: Validate agent exists
    
    # TODO: Return agent name for routing
    
    return "weather"  # Placeholder

def final_coordinator(state: TravelPlanState) -> dict:
    """
    Final coordination node that combines all agent responses into comprehensive plan.
    
    Args:
        state: Travel planning state with all agent responses
        
    Returns:
        Updated state with final travel plan
        
    TODO: Implement final coordination logic
    - Collect responses from all agents in state.agent_responses
    - Combine weather, flight, accommodation, activities, and budget data
    - Create comprehensive travel plan with:
        * Executive summary
        * Weather forecast and packing list
        * Flight recommendations and booking links
        * Accommodation options with pros/cons
        * Daily itinerary suggestions
        * Budget breakdown and total cost estimate
    - Add final plan as AIMessage to state.messages
    - Set planning_complete = True
    """
    # TODO: Collect all agent responses
    
    # TODO: Combine data into comprehensive travel plan
    
    # TODO: Create executive summary
    
    # TODO: Format final recommendations
    
    # TODO: Add final plan to conversation
    
    # TODO: Mark planning as complete
    
    return {
        "messages": [AIMessage(content="TODO: Implement final travel plan coordination")],
        "planning_complete": True
    } 