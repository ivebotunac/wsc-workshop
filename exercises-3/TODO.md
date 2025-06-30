# Exercise 3: Travel Planning Supervisor Agent

## Overview
In this exercise, you'll implement a **Supervisor Agent Pattern** that coordinates multiple specialized agents to create comprehensive travel plans. This builds upon the weather agent from Exercise 2 by adding it to a multi-agent system.

## Official LangGraph tutorial:
[LangGraph Supervisor tutorial](https://langchain-ai.github.io/langgraph/how-tos/supervisor/)

## What You'll Build
A travel planning supervisor that coordinates:
- **Weather Agent** (from Exercise 2) - analyzes weather forecasts
- **Flight Agent** - searches for flights and prices  
- **Accommodation Agent** - finds hotels and lodging options
- **Activities Agent** - discovers local attractions and activities
- **Budget Agent** - calculates costs and provides recommendations

## System Architecture

### Supervisor Pattern Flow
```
USER REQUEST → SUPERVISOR → [Weather, Flight, Hotel, Activities, Budget] → SUPERVISOR → FINAL PLAN
```

### Key Components:
1. **Supervisor Node** - Routes tasks to appropriate agents and coordinates results
2. **Specialized Agents** - Each handles a specific domain (weather, flights, etc.)
3. **Shared State** - Accumulates information from all agents
4. **Final Coordinator** - Combines all results into a comprehensive travel plan

## Files to Implement

### 1. `state.py`
Define state schemas for:
- `TravelPlanState` - Main supervisor state
- `AgentResponse` - Standardized agent response format

### 2. `tools.py`  
Implement search tools for each agent:
- `search_weather_info()` - Weather data (reuse from Exercise 2)
- `search_flights()` - Flight information and prices
- `search_accommodation()` - Hotels and lodging options
- `search_activities()` - Local attractions and things to do
- `search_budget_info()` - Cost information and budget tips

### 3. `travel_agents.py`
Implement specialized agent functions:
- `weather_agent()` - Weather analysis
- `flight_agent()` - Flight research
- `accommodation_agent()` - Lodging search
- `activities_agent()` - Activity recommendations
- `budget_agent()` - Cost calculations

### 4. `supervisor.py`
Implement supervisor logic:
- `supervisor_node()` - Routes tasks to appropriate agents
- `create_supervisor_chain()` - Sets up the supervisor LLM chain
- `should_continue()` - Decides when planning is complete

### 5. `workflow.py`
Build the supervisor workflow:
- `create_travel_supervisor_workflow()` - Main workflow construction
- Connect supervisor to all agents with conditional routing

### 6. `run.py`
Complete the main execution:
- Interactive loop for travel planning requests
- State initialization and result formatting

## Supervisor Decision Logic

The supervisor should be able to:
1. **Parse user requests** - Understand what travel information is needed
2. **Route to agents** - Decide which agents should handle which parts
3. **Coordinate results** - Collect and organize information from agents
4. **Quality control** - Check if all necessary information is gathered
5. **Final synthesis** - Create comprehensive travel recommendations

## Agent Specialization

### Weather Agent
- Analyze weather forecasts for travel dates
- Provide packing recommendations
- Suggest weather-appropriate activities

### Flight Agent  
- Search for flight options and prices
- Compare airlines and routes
- Provide booking recommendations

### Accommodation Agent
- Find hotels, hostels, and alternative lodging
- Compare prices and amenities
- Check availability for travel dates

### Activities Agent
- Discover local attractions and experiences
- Find restaurants and entertainment
- Suggest itineraries based on interests

### Budget Agent
- Calculate total trip costs
- Provide budget breakdowns
- Suggest cost-saving tips

## Environment Setup
Make sure you have your `.env` file with:
```
OPENAI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```