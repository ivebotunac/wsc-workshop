# Main runner for the weather agent
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from workflow import create_weather_workflow

def main():
    """Main function - creates workflow and runs interactive loop."""
    # Load environment variables from .env file
    load_dotenv()
    
    # Create the weather workflow
    app = create_weather_workflow()
    
    # Start interactive chat loop
    print("🌤️ Weather Agent")
    print("Ask about weather in any city!")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'q', 'exit']:
            break
        
        # Process user input through the workflow
        if user_input:
            print("\n🔍 Getting weather...")
            
            # Create initial state and run workflow
            initial_state = {"messages": [HumanMessage(content=user_input)]}
            result = app.invoke(initial_state)
            
            # Display the weather information
            print(f"\nAgent:\n {result['messages'][-1].content}\n")

if __name__ == "__main__":
    main() 