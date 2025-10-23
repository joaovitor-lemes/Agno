from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools

from dotenv import load_dotenv

from agno.os import AgentOS
from agno.db.sqlite import SqliteDb

load_dotenv()

def celsius_to_fh(temp_celsius: float) -> float:
    """Converte temperatura de Celsius para Fahrenheit."""
    return (temp_celsius * 9 / 5) + 32

agent = Agent(name="primeiro",
    model=OpenAIChat(
        id="gpt-4.1-mini",  
    ),
    tools=[TavilyTools(), celsius_to_fh],
    db=SqliteDb(db_file="agno.db"),
    add_history_to_context=True,
    num_history_runs=5
    
)


# agent.print_response("Qual a temperatura de Goiânia hoje em celsius e fahrenheit?")

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__=="__main__":
    agent_os.serve(app = "3_own_tools:app", reload = True)



