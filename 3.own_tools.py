from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()

def celsius_to_fh(temp_celsius: float) -> float:
    """Converte temperatura de Celsius para Fahrenheit."""
    return (temp_celsius * 9 / 5) + 32

agent = Agent(
    model=OpenAIChat(
        id="gpt-4.1-mini",  
    ),
    tools=[TavilyTools(), celsius_to_fh],
    
)

# 🔹 Faz a pergunta
agent.print_response("Qual a temperatura de Goiânia hoje em celsius e fahrenheit?")





