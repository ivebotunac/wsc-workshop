# Weather agent node functions for LangGraph workflow
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from state import WeatherResearchState
from tools import get_weather_with_tavily

class WeatherResearchAgent:
    """Weather research agent with node functions for LangGraph workflow."""
    
    def __init__(self):
        # Initialize OpenAI model for formatting weather data
        self.model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
    
    def get_weather_node(self, state: WeatherResearchState) -> dict:
        """First node: Get raw weather data from Tavily"""
        city = str(state["messages"][-1].content).strip()
        
        # Fetch raw weather data using Tavily search
        raw_weather = get_weather_with_tavily(city)
        
        return {"messages": [AIMessage(content=raw_weather)]}
    
    def format_weather_node(self, state: WeatherResearchState) -> dict:
        """Second node: Format raw weather data using OpenAI"""
        raw_weather = str(state["messages"][-1].content)
        
        # Create prompt for OpenAI to format the data
        prompt = f"""
        Format this weather information in a clean, readable way:
        
        {raw_weather}
        
        Return only the essential weather information in this format:
        🌤️ Weather in [City]:
        • Temperature: [temp]
        • Condition: [condition] 
        • Details: [brief description]
        """
        
        # Get formatted response from OpenAI
        response = self.model.invoke([HumanMessage(content=prompt)])
        
        return {"messages": [response]} 