# Weather research workflow definition
from langgraph.graph import StateGraph, START, END
from weather_agent import WeatherResearchAgent
from state import WeatherResearchState

def create_weather_workflow():
    """Create and return the compiled weather research workflow."""
    # Initialize agent with node functions
    agent = WeatherResearchAgent()
    
    # Create workflow graph
    workflow = StateGraph(WeatherResearchState)
    
    # Add nodes
    workflow.add_node("weather", agent.get_weather_node)
    workflow.add_node("format", agent.format_weather_node)
    
    # Define flow: START -> weather -> format -> END
    workflow.add_edge(START, "weather")
    workflow.add_edge("weather", "format")
    workflow.add_edge("format", END)
    
    return workflow.compile() 