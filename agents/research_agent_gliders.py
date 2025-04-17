## Code for the Agent
from datetime import datetime
from textwrap import dedent
import prompt_formats

from agno.agent import Agent 
from agno.models.openai import OpenAIChat 
from agno.models.groq import Groq 
from agno.tools.exa import ExaTools
from agno.tools.arxiv import ArxivTools 

#Environmental Imports
import os
from dotenv import load_dotenv 

load_dotenv() 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["EXA_API_KEY"] = os.getenv("EXA_API_KEY")


# Agent Customization
research_scholar = Agent(
    model = OpenAIChat(id="gpt-4o"),
    tools = [
        ArxivTools(search_arxiv=True, read_arxiv_papers=True, download_dir="C:\\Users\\ravic\\projects\\tmp\\download_papers"),
        ExaTools(start_published_date=datetime.now().strftime("%Y-%m-%d"),type="keyword")
        ],
    description = dedent(prompt_formats.description_format),
    instructions = dedent(prompt_formats.instruction_format),
    expected_output=dedent(prompt_formats.output_format),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    save_response_to_file="/tmp/{paper_title}.md",                                             
)

# Example usage with academic research request

prompt = dedent(prompt_formats.question_prompt)

if __name__=="__main__":
    research_scholar.print_response(prompt, stream=True)
