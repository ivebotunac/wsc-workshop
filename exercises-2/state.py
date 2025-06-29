# State schema for REACT weather agent workflow
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

# REACT agent state following LangGraph tutorial pattern
class WeatherReactState(TypedDict):
    """
    State class that holds:
    - messages: sequence of messages throughout the workflow (with reducer)
    """
    messages: Annotated[Sequence[BaseMessage], add_messages] 