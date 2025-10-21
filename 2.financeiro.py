from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq
from dotenv import load_dotenv
import os 

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")


agent = Agent( model = Groq(id = "llama-3.3-70b-versatile"), 
              tools = [YFinanceTools()],
                instructions = "Apresente em ordem decrescente" ) 


agent.print_response("gere um gráfico de linha dos ultimos 10 dias das ações do itau", stream = True)