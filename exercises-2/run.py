# Main runner for the REACT weather agent
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from workflow import create_weather_react_workflow

def print_stream(stream):
    """Helper function for formatting the stream nicely (from LangGraph tutorial)"""
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

def main():
    """
    Main function - creates REACT workflow and runs interactive loop.
    Following LangGraph tutorial pattern with streaming support.
    """
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Create the REACT weather workflow
    app = create_weather_react_workflow()
    
    # Start interactive chat loop
    print("🌤️ REACT Weather Agent")
    print("Ask about weather in any city! I can search for additional information if needed.")
    print("Type 'quit' to exit\n")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'q', 'exit']:
            break
        
        # Process user input through the REACT workflow
        if user_input:
            print("\n🔍 REACT Agent processing...")
            
            # Create initial state with user message (following tutorial pattern)
            inputs = {"messages": [HumanMessage(content=user_input)]}
            
            # Stream the workflow execution (following tutorial)
            print_stream(app.stream(inputs, stream_mode="values"))
            print()

if __name__ == "__main__":
    main() 