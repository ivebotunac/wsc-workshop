# WSC Workshop

LangGraph workshop exercises for learning agent development patterns.

## Exercise 1: Simple Weather Agent
A basic weather agent that demonstrates linear LangGraph workflows:
- **Pattern**: Linear workflow (START → weather → format → END)
- **Nodes**: 2 nodes (weather data fetching, response formatting)
- **State**: Simple message-based state management
- **Tools**: Tavily search for weather data
- **Model**: OpenAI GPT-4o-mini for response formatting

Students learn fundamental concepts:
- State management with typed dictionaries
- Node functions and workflow construction
- External API integration
- Basic LangGraph patterns

## Exercise 2: REACT Weather Agent (Skeleton)
An advanced weather agent implementing the REACT (Reason, Act, Observe) pattern:
- **Pattern**: Conditional workflow with iterative decision making
- **Nodes**: 4 nodes (reasoning, weather action, search action, formatting)
- **State**: Enhanced state with action tracking
- **Tools**: Multiple tools for weather and general search
- **Model**: OpenAI GPT-4o-mini for reasoning and formatting

Students implement:
- Conditional edge functions
- Multi-step reasoning workflows
- Dynamic tool selection
- Complex state management
- Agent decision-making patterns

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Create `.env` file with API keys:
   ```
   OPENAI_API_KEY=your_key_here
   TAVILY_API_KEY=your_key_here
   ```
3. Run exercises: `python run.py` in each exercise directory