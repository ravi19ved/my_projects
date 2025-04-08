from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq 
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv 
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

