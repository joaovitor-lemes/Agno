from agno.agent import Agent
from agno.tools.models.groq import GroqTools
from dotenv import load_dotenv
import os



load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

agent = Agent(
    instructions=[
        "You are a helpful assistant that can transcribe audio, translate text and generate speech."
    ],
    tools=[GroqTools(api_key= groq_api_key)]
    )



