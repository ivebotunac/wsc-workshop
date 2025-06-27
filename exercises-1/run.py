# Main runner for the weather agent
from dotenv import load_dotenv

from weather_agent import WeatherResearchAgent

def main():
    """Main function - creates agent and runs interactive loop"""
    # Load environment variables (.env file)
    load_dotenv()
    
    # Initialize the weather agent
    agent = WeatherResearchAgent()
    
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
            result = agent.invoke(user_input)
            print(f"\nAgent:\n {result['messages'][-1].content}\n")

if __name__ == "__main__":
    main() 