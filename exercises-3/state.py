# State schemas for Travel Planning Supervisor Agent
from typing import TypedDict, Annotated, Sequence, Optional
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class TravelPlanState(TypedDict):
    """
    Simple state structure for supervisor workflow.
    """
    # Conversation history
    messages: Annotated[Sequence[BaseMessage], add_messages]
    
    # Which agent should work next
    next_agent: Optional[str]
    
    # Whether planning is complete
    planning_complete: bool 