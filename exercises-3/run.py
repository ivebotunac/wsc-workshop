# Main execution script for Travel Planning Supervisor Agent
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from .workflow import create_travel_supervisor_workflow, initialize_travel_state

def print_travel_plan_results(final_state):
    """
    Print the final travel plan results in a formatted way.
    
    Args:
        final_state: Final state from workflow execution
        
    TODO: Implement result formatting
    - Extract agent responses from final_state
    - Print organized travel plan with sections for:
        * Weather forecast and packing recommendations
        * Flight options and booking details
        * Accommodation recommendations  
        * Activities and itinerary suggestions
        * Budget breakdown and cost estimates
    - Format output to be easy to read and actionable
    """
    # TODO: Extract final conversation messages
    
    # TODO: Extract agent responses if available
    
    # TODO: Format and print travel plan sections
    
    # TODO: Print final recommendations
    
    print("TODO: Implement travel plan formatting")

def main():
    """
    Main function to run the travel planning supervisor workflow.
    
    TODO: Implement main execution logic
    - Load environment variables for API keys
    - Create the travel supervisor workflow
    - Run interactive loop for travel planning requests
    - For each request:
        * Initialize travel state from user input
        * Execute workflow to completion
        * Print formatted travel plan results
    - Handle user input for new requests or exit
    """
    
    # TODO: Load environment variables
    
    # TODO: Verify required API keys are present
    
    # TODO: Create travel supervisor workflow
    
    print("🌍 Travel Planning Supervisor Agent")
    print("=" * 50)
    print("Ask me to plan your next trip! Include:")
    print("- Destination")
    print("- Travel dates (optional)")
    print("- Budget constraints (optional)")
    print("- Any special interests or requirements")
    print("\nExample: 'Plan a 5-day trip to Paris in March with a $2000 budget'")
    print("Type 'quit' to exit\n")
    
    while True:
        # TODO: Get user input for travel request
        
        # TODO: Check for exit conditions
        
        # TODO: Initialize travel state from user request
        
        # TODO: Execute supervisor workflow
        
        # TODO: Print formatted travel plan results
        
        # TODO: Ask if user wants to plan another trip
        
        print("\n" + "=" * 50)

def test_single_request():
    """
    Test function for development - runs a single travel planning request.
    
    TODO: Implement test function
    - Load environment variables
    - Create workflow
    - Test with sample request like "Plan a weekend trip to Barcelona"
    - Print results
    - Use this for debugging and development
    """
    # TODO: Load environment and create workflow
    
    # TODO: Create test request
    
    # TODO: Initialize state and run workflow
    
    # TODO: Print results
    
    print("TODO: Implement test function")

if __name__ == "__main__":
    # TODO: Choose between main() and test_single_request()
    # Use test_single_request() during development
    # Use main() for interactive experience
    
    # Uncomment one of these:
    # test_single_request()
    # main()
    
    print("TODO: Choose execution mode (main or test)") 