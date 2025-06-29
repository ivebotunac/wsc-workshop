# State schema for REACT weather agent workflow
from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage

# TODO: Implement function to combine message lists
def add_messages(left: List[BaseMessage], right: List[BaseMessage]) -> List[BaseMessage]:
    """
    Function to combine two lists of messages.
    You need to return the combined list of messages.
    """
    # Your code here:
    return []  # Replace with proper implementation

# TODO: Define state class for REACT agent
class WeatherReactState(TypedDict):
    """
    State class that holds:
    - messages: list of messages throughout the workflow
    - next_action: next action the agent should take ("weather", "search", "decide", or "end")
    """
    # Define the required fields here:
    pass 