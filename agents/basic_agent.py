from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["Groq_API_KEY"] = os.getenv("Groq_API_KEY")

agent = Agent(
    model = OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for story telling",
    markdown = True
)

agent.print_response("Tell me about a breaking news story from Hyderabad, Telangana")