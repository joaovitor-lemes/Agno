from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
from dotenv import load_dotenv
import os 


load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

print(tavily_api_key)
print(groq_api_key)

agent = Agent( model = Groq(id = "llama-3.3-70b-versatile"), 
              tools = [TavilyTools(api_key=tavily_api_key)] ) 


agent.print_response("qual a temperatura atual de Goiania hoje")

