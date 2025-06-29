# Exercise 2: REACT Weather Agent

## Overview
In this exercise, you'll implement a REACT (Reason, Act, Observe) pattern weather agent that can make iterative decisions and multiple tool calls based on user requests.

## What You'll Build
A weather agent that can:
- Reason about what information is needed
- Take actions (weather search, additional research)
- Observe results and decide next steps
- Format final responses

## Files to Implement

### 1. `state.py`
- Complete the `add_messages()` function
- Define the `WeatherReactState` TypedDict with:
  - `messages`: List of conversation messages
  - `next_action`: String indicating next action ("weather", "search", "decide", "end")

### 2. `tools.py`  
- Implement `get_weather_with_tavily()` for weather searches
- Implement `search_additional_info()` for general searches

### 3. `weather_agent.py`
- Implement the `reasoning_node()` that decides next actions
- Implement `weather_action_node()` that gets weather data
- Implement `search_action_node()` that searches for additional info
- Implement `format_response_node()` that creates final responses

### 4. `workflow.py`
- Implement `should_continue()` conditional edge function
- Complete `create_weather_react_workflow()` with nodes and edges

### 5. `run.py`
- Complete the main() function to run the interactive loop

## REACT Pattern Flow
```
START -> reasoning -> [weather/search/format] -> reasoning -> ... -> END
```

The agent should be able to:
1. Analyze user requests
2. Decide if it needs weather data, additional search, or can format a response
3. Execute the chosen action
4. Return to reasoning to decide next steps
5. Continue until it has enough information to provide a final answer

## Environment Setup
Make sure you have your `.env` file with:
```
OPENAI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

## Test Your Implementation
Try queries like:
- "What's the weather in Paris?"
- "Compare weather in London and New York"
- "What's the weather like in Tokyo and what should I pack?" 