from agno.agent import Agent 
from agno.models.openai import OpenAIChat 
from agno.models.groq import Groq 
from agno.tools.duckduckgo import DuckDuckGoTools 

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
    model= OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for story telling",
    tools = [DuckDuckGoTools()],
    show_tool_calls=True,
    markdown = True
)

agent.print_response("Tell me about a breaking news story from Hyderabad, Telangana")

