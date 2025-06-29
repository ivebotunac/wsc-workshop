# REACT Weather agent node functions following LangGraph tutorial
import json
from langchain_core.messages import ToolMessage, SystemMessage, AIMessage
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI

from state import WeatherReactState
from tools import tools

class WeatherReactAgent:
    """REACT weather agent following LangGraph tutorial pattern."""
    
    def __init__(self):
        # Initialize OpenAI model and bind tools (following tutorial)
        self.model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
        self.model = self.model.bind_tools(tools)
        
        # Create tools lookup dictionary
        self.tools_by_name = {tool.name: tool for tool in tools}
    
    def call_model(self, state: WeatherReactState) -> dict:
        """
        REACT call_model node: Calls the LLM to decide next action.
        
        Following LangGraph tutorial pattern - this node calls the model
        which can decide to use tools or provide final response.
        """
        # System prompt for weather assistant
        system_prompt = SystemMessage(
            "You are a helpful weather assistant. You can get weather information and search for additional details. "
            "Use the available tools when needed to provide accurate and helpful weather information to users."
        )
        
        # Call model with system prompt + conversation history
        response = self.model.invoke([system_prompt] + list(state["messages"]))
        
        # Return as list to be added to existing messages
        return {"messages": [response]}
    
    def tool_node(self, state: WeatherReactState) -> dict:
        """
        REACT tool_node: Executes the tools requested by the model.
        
        Following LangGraph tutorial pattern - processes tool calls from the model.
        """
        outputs = []
        last_message = state["messages"][-1]
        
        # Process each tool call from the last message (only for AIMessage)
        if isinstance(last_message, AIMessage) and hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            for tool_call in last_message.tool_calls:
                tool_result = self.tools_by_name[tool_call["name"]].invoke(tool_call["args"])
                outputs.append(
                    ToolMessage(
                        content=json.dumps(tool_result) if not isinstance(tool_result, str) else tool_result,
                        name=tool_call["name"],
                        tool_call_id=tool_call["id"],
                    )
                )
        
        return {"messages": outputs}
    
    def should_continue(self, state: WeatherReactState) -> str:
        """
        REACT conditional edge: Determines whether to continue with tools or end.
        
        Following LangGraph tutorial pattern - checks if model wants to use tools.
        """
        messages = state["messages"]
        last_message = messages[-1]
        
        # If there are tool calls, continue to tools
        if isinstance(last_message, AIMessage) and hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            return "continue"
        # Otherwise, end the conversation
        else:
            return "end" 