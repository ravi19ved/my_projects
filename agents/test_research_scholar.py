
## Code for the Agent

from datetime import datetime
from textwrap import dedent

from agno.agent import Agent 
from agno.models.openai import OpenAIChat 
from agno.models.groq import Groq 
from agno.tools.exa import ExaTools
from agno.tools.arxiv import ArxivTools  

import os
from dotenv import load_dotenv 

load_dotenv() 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["EXA_API_KEY"] = os.getenv("EXA_API_KEY")

test_research_agent = Agent(
    name="research_scholar",
    model = OpenAIChat(id="gpt-4o"),
    tools = [ExaTools(start_published_date=datetime.now().strftime("%Y-%m-%d"),type="keyword"), 
             ArxivTools(search_arxiv=True, read_arxiv_papers=True, download_dir="./tmp/papers_download")],
    description="An AI research assistant designed to write high-quality academic papers based on scientific literature.",
    expected_output="A detailed research article or literature review, written in an academic tone, containing citations in APA format, including a full reference list.",
    instructions=("""
You are a research scholar AI trained to write scientific papers suitable for peer-reviewed journals. Your task is to:
1. Analyze the provided topic or prompt.
2. Research existing academic and scientific literature (simulated or retrieved via tools).
3. Write a detailed and structured scientific article, including the following sections:
   - Abstract
   - Introduction
   - Literature Review
   - Methodology (if applicable)
   - Results and Discussion (if applicable)
   - Conclusion
   - References (APA format)
4. Provide in-text citations for all factual, statistical, or theoretical claims.
5. Format the entire article in a publication-ready tone.
6. Use APA-style citations both in-text and in the reference list.
7. If exact papers are not supplied, simulate realistic references using plausible titles, authors, journals, and years.

Ensure that:
- The article is self-contained and logically structured.
- The tone is professional and academic.
- No unsupported claims are made.
- The reference list matches the in-text citations.
"""),
markdown=True,
show_tool_calls=True,
add_datetime_to_instructions=True,
save_response_to_file="tmp/{message}.md", 
)

prompt = dedent("""Write a research paper titled "The Role of Autonomous Underwater Vehicles in Coastal Oceanography". Focus on:
- The evolution and importance of AUVs.
- Comparison of AUVs like Slocum gliders, SeaGliders, and hybrid ROVs.
- Recent missions and case studies.
- Challenges in coastal operations.
- A conclusion about future directions.

Include APA citations throughout and provide a reference list at the end.""")

test_research_agent.print_response(prompt, stream=True)
