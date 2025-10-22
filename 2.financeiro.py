from agno.agent import Agent

from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq
from dotenv import load_dotenv
import os 

# Agente de IA que informa sobre as finaças em geral

load_dotenv()

# groq_api_key = os.getenv("GROQ_API_KEY")


agent = Agent( model = Groq(id = "llama-3.3-70b-versatile"), 
              tools = [YFinanceTools()],
                instructions = "Apresente em ordem decrescente" ) 


agent.print_response("gere um gráfico de linha dos ultimos 10 dias das ações do itau", stream = True)