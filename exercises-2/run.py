# Main runner for the REACT weather agent
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from workflow import create_weather_react_workflow

# TODO: Implement main function
def main():
    """
    Main function - creates REACT workflow and runs interactive loop.
    
    This function should:
    1. Load environment variables
    2. Create the REACT weather workflow
    3. Run an interactive chat loop
    4. Handle user input and display agent responses
    """
    
    # TODO: Load environment variables from .env file
    # Your code here:
    
    # TODO: Create the REACT weather workflow
    # Your code here:
    
    # TODO: Start interactive chat loop
    print("🌤️ REACT Weather Agent")
    print("Ask about weather in any city! I can search for additional information if needed.")
    print("Type 'quit' to exit\n")
    
    while True:
        # TODO: Get user input
        # Your code here:
        
        # TODO: Check for exit commands
        # Your code here:
        
        # TODO: Process user input through the REACT workflow
        # Hint: Create initial state with user message and next_action="decide"
        # Your code here:
        
        # TODO: Display the final response
        # Your code here:
        
        pass

if __name__ == "__main__":
    main() 