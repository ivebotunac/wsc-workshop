# REACT weather workflow definition following LangGraph tutorial
from langgraph.graph import StateGraph, END
from weather_agent import WeatherReactAgent
from state import WeatherReactState

def create_weather_react_workflow():
    """
    Create and return the compiled REACT weather workflow.
    
    Following LangGraph tutorial pattern:
    - agent node calls the model
    - tools node executes tools
    - conditional edge decides next step
    """
    # Initialize agent
    agent = WeatherReactAgent()
    
    # Create StateGraph with WeatherReactState
    workflow = StateGraph(WeatherReactState)
    
    # Add nodes following tutorial pattern
    workflow.add_node("agent", agent.call_model)
    workflow.add_node("tools", agent.tool_node)
    
    # Set entry point to agent (following tutorial)
    workflow.set_entry_point("agent")
    
    # Add conditional edge from agent
    workflow.add_conditional_edges(
        # Start node
        "agent",
        # Function that determines next node
        agent.should_continue,
        # Mapping of outputs to nodes
        {
            # If tools needed, go to tools node
            "continue": "tools",
            # If done, end workflow
            "end": END,
        },
    )
    
    # Add normal edge from tools back to agent (following tutorial)
    workflow.add_edge("tools", "agent")
    
    # Compile and return workflow
    return workflow.compile() 