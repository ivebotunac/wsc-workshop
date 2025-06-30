# State schemas for Travel Planning Supervisor Agent
from typing import TypedDict, Annotated, Sequence, List, Optional
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentResponse(TypedDict):
    """
    Standardized response format that all specialized agents should return.
    This ensures consistent data structure across all agents.
    """
    agent_name: str        # Name of the agent that provided this response
    status: str            # "success", "partial", "failed"
    data: dict             # Agent-specific data (weather info, flight details, etc.)
    summary: str           # Human-readable summary of findings

class TravelPlanState(TypedDict):
    """
    Main state for the travel planning supervisor workflow.
    
    TODO: Define the state structure that will hold:
    - messages: Conversation history with add_messages reducer
    - destination: Target travel destination
    - travel_dates: When the user wants to travel
    - budget: Budget constraints if specified
    - agent_responses: Responses from all specialized agents
    - next_agent: Which agent should be called next
    - planning_complete: Whether all necessary information is gathered
    """
    # TODO: Add messages field with proper annotation and reducer
    messages: ...
    
    # TODO: Add destination field to track where user wants to travel
    destination: ...
    
    # TODO: Add travel_dates field for date constraints
    travel_dates: ...
    
    # TODO: Add budget field for budget constraints  
    budget: ...
    
    # TODO: Add agent_responses to store responses from all agents
    agent_responses: ...
    
    # TODO: Add next_agent to track routing decisions
    next_agent: ...
    
    # TODO: Add planning_complete boolean flag
    planning_complete: ... 