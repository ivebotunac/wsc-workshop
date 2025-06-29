# State schema for the weather agent workflow
from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage

# Helper function to combine message lists
def add_messages(left: List[BaseMessage], right: List[BaseMessage]) -> List[BaseMessage]:
    return left + right

# State holds conversation messages throughout the workflow
class WeatherResearchState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]