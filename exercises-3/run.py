# Main execution script for Travel Planning Supervisor Agent
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from workflow import create_travel_supervisor_workflow, initialize_travel_state

def print_travel_plan_results(final_state):
    """Prints final travel plan results in formatted way"""
    
    print("\n" + "="*60)
    print("🎯 TRAVEL PLAN RESULTS")
    print("="*60)
    
    # Print all messages from conversation
    for i, msg in enumerate(final_state["messages"]):
        if hasattr(msg, 'content') and msg.content:
            print(f"\n--- Step {i+1} ---")
            print(msg.content)
    
    print("\n" + "="*60)

def main():
    """Main function to run the travel planning supervisor workflow"""
    
    # Load environment variables
    load_dotenv()
    
    # Check if required API keys are present
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY is required in .env file")
        return
    
    if not os.getenv("TAVILY_API_KEY"):
        print("❌ TAVILY_API_KEY is required in .env file")
        return
    
    # Create travel supervisor workflow
    workflow = create_travel_supervisor_workflow()
    
    print("🌍 Travel Planning Supervisor Agent")
    print("=" * 50)
    print("Ask me to plan your next trip! Include:")
    print("- Destination")
    print("- Travel dates (optional)")
    print("- Budget constraints (optional)")
    print("- Any special interests or requirements")
    print("Type 'quit' to exit\n")
    
    while True:
        # Get user input for travel request
        user_input = input("Your travel request: ").strip()
        
        # Check for exit conditions
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye! 🌟")
            break
        
        if not user_input:
            print("Please enter a travel request.")
            continue
        
        try:
            # Initialize travel state from user request
            initial_state = initialize_travel_state(user_input)
            
            print(f"\n🔄 Processing your request: '{user_input}'")
            print("Please wait while supervisor coordinates agents...\n")
            
            # Execute supervisor workflow
            final_state = workflow.invoke(initial_state)
            
            # Print formatted travel plan results
            print_travel_plan_results(final_state)
            
        except Exception as e:
            print(f"❌ Error during processing: {str(e)}")
        
        # Ask if user wants to plan another trip
        print("\n" + "="*50)
        another = input("Would you like to plan another trip? (y/n): ").strip().lower()
        if another not in ['y', 'yes']:
            print("Goodbye! 🌟")
            break

if __name__ == "__main__":
    main() 