# Travel Planning Supervisor Workflow
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from state import TravelPlanState
from agents import AVAILABLE_AGENTS
from supervisor import supervisor_node, should_continue, route_to_agent, final_coordinator

def create_travel_supervisor_workflow():
    """Creates travel planning supervisor workflow with all agents and routing"""
    
    # Create StateGraph with TravelPlanState
    workflow = StateGraph(TravelPlanState)
    
    # Add supervisor node
    workflow.add_node("supervisor", supervisor_node)
    
    # Add all specialized agent nodes
    for agent_name, agent_func in AVAILABLE_AGENTS.items():
        workflow.add_node(agent_name, agent_func)
    
    # Add final coordinator node
    workflow.add_node("final_coordinator", final_coordinator)
    
    # Set entry point to supervisor
    workflow.set_entry_point("supervisor")
    
    # Add conditional edge from supervisor for continue/end decision
    workflow.add_conditional_edges(
        "supervisor",
        should_continue,
        {
            "continue": "agent_router",
            "end": "final_coordinator"
        }
    )
    
    # Add router node that will dynamically route to appropriate agent
    def router_node(state):
        return {"next_agent": route_to_agent(state)}
    
    workflow.add_node("agent_router", router_node)
    
    # Add conditional edges from router to all agents
    workflow.add_conditional_edges(
        "agent_router",
        route_to_agent,
        {
            "weather": "weather",
            "flight": "flight", 
            "accommodation": "accommodation",
            "activities": "activities",
            "budget": "budget"
        }
    )
    
    # Add edges from each agent back to supervisor
    for agent_name in AVAILABLE_AGENTS.keys():
        workflow.add_edge(agent_name, "supervisor")
    
    # Add edge from final coordinator to END
    workflow.add_edge("final_coordinator", END)
    
    # Compile and return workflow
    return workflow.compile()

def initialize_travel_state(user_request: str) -> dict:
    """Initializes travel planning state from user request"""
    
    return {
        "messages": [HumanMessage(content=user_request)],
        "next_agent": None,
        "planning_complete": False
    } 