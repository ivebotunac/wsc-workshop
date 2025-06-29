# REACT Weather agent node functions for LangGraph workflow
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from state import WeatherReactState
from tools import get_weather_with_tavily, search_additional_info

class WeatherReactAgent:
    """REACT weather agent with node functions for iterative decision making."""
    
    def __init__(self):
        # Initialize OpenAI model for reasoning and decision making
        self.model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
    
    # TODO: Implement reasoning node
    def reasoning_node(self, state: WeatherReactState) -> dict:
        """
        REACT Reasoning Node: Analyze the current state and decide next action.
        
        This node should:
        1. Look at the conversation history
        2. Determine what information is needed
        3. Decide the next action: "weather", "search", or "end"
        4. Update the state with the decision
        
        Returns:
            Updated state with next_action field
        """
        # Your code here:
        return {}  # Replace with proper implementation
    
    # TODO: Implement weather action node
    def weather_action_node(self, state: WeatherReactState) -> dict:
        """
        Action Node: Get weather information for the requested city.
        
        This node should:
        1. Extract city name from the latest message
        2. Call get_weather_with_tavily() tool
        3. Add the weather result to messages
        4. Set next_action to "decide" for next reasoning step
        
        Returns:
            Updated state with weather information and next action
        """
        # Your code here:
        return {}  # Replace with proper implementation
    
    # TODO: Implement search action node  
    def search_action_node(self, state: WeatherReactState) -> dict:
        """
        Action Node: Search for additional information.
        
        This node should:
        1. Determine what additional info is needed
        2. Call search_additional_info() tool
        3. Add search results to messages
        4. Set next_action to "decide" for next reasoning step
        
        Returns:
            Updated state with search results and next action
        """
        # Your code here:
        return {}  # Replace with proper implementation
    
    # TODO: Implement final formatting node
    def format_response_node(self, state: WeatherReactState) -> dict:
        """
        Final Node: Format the collected information into a user-friendly response.
        
        This node should:
        1. Combine all gathered information
        2. Use the LLM to format a final response
        3. Set next_action to "end"
        
        Returns:
            Final formatted response
        """
        # Your code here:
        return {}  # Replace with proper implementation 