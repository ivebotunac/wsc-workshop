# Weather agent with LangGraph workflow
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from state import WeatherResearchState
from tools import get_weather_with_tavily

class WeatherResearchAgent:
    def __init__(self):
        # Initialize OpenAI model for formatting
        self.model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
        # Build and compile the workflow
        self.app = self._build_workflow().compile()
    
    def get_weather_node(self, state: WeatherResearchState) -> dict:
        """First node: Get raw weather data from Tavily"""
        city = str(state["messages"][-1].content).strip()
        
        # Fetch raw weather data using Tavily search
        raw_weather = get_weather_with_tavily(city)
        
        # Pass raw data to next node
        return {"messages": [AIMessage(content=raw_weather)]}
    
    def format_weather_node(self, state: WeatherResearchState) -> dict:
        """Second node: Format raw weather using OpenAI"""
        raw_weather = str(state["messages"][-1].content)
        
        # Prompt to clean up weather data
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
    
    def _build_workflow(self) -> StateGraph:
        """Build LangGraph workflow: weather -> format"""
        workflow = StateGraph(WeatherResearchState)
        
        # Add two nodes to the workflow
        workflow.add_node("weather", self.get_weather_node)
        workflow.add_node("format", self.format_weather_node)
        
        # Define workflow edges: START -> weather -> format -> END
        workflow.add_edge(START, "weather")
        workflow.add_edge("weather", "format") 
        workflow.add_edge("format", END)
        
        return workflow
    
    def invoke(self, message: str) -> dict:
        """Run the workflow with user input"""
        initial_state = {"messages": [HumanMessage(content=message)]}
        return self.app.invoke(initial_state) 