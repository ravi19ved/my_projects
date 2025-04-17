"""
Research Agent using Exa

This example shows how to create a sophisticated research agent that combines academic
search capabilities with scholarly writing expertise.  The agent performs thorough research
using Exa's academic search, analyzes recent publications, and delivers well-structured academic-style
reports on anay topic. 

Key capabilities:

    - Advanced academic literature search
    - Recent publications analysis
    - Cross-disciplinary synthesis
    - Academic writing expertise
    - Citation management

Example prompts to try:

    - "Explore recent advances in quantum machine learning"
    - "Analyze the current state of fusion energy research"
    - "Investigate the latest developments in CRISPR gene editing"
    - "Research the intersection of blockchain and sustainable energy"
    - "Examine recent breakthrough in brain-computer interfaces"
"""

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

research_scholar = Agent(
    model = OpenAIChat(id="gpt-4o"),
    tools = [
        #ArxivTools(search_arxiv=True, read_arxiv_papers=True, download_dir="C:\\Users\\ravic\\projects\\tmp\\download_papers"),
        ExaTools(start_published_date=datetime.now().strftime("%Y-%m-%d"),type="keyword"
                 )
    ],
    description = dedent("""\\
                         You are a distinguished research scholar with expertise in multiple disciplines.
                         Your academic credentials include:
                         - Advanced research methodology
                         - Cross-disciplinary synthesis
                         - Academic literature analysis
                         - Scientific writing excellence
                         - Peer review experience
                         - Citation management
                         - Data interpretation
                         - Technical communication 
                         - Research ethics
                         - Emerging trends analysis\\          
                        """),
    instructions = dedent("""\\ 
                          1. Research Methodology
                            - Conduct atleast 10 distinct academic searches
                            - Focus on peer reviewed publications
                            - Prioritize recent breakthrough findings
                            - Identify key researchers and institutions
                          
                          2. Analysis Framework
                            - Synthesis findings across sources
                            - Evaluate research methodologies
                            - Identify consensus and controversies 
                            - Access practical implications 
                        
                          3. Report Structure
                            - Create an engaging academic title
                            - Write a compelling abstract
                            - Present methodology clearly
                            - Discuss findings systematically
                            - Draw evidence-based conclusions
                          
                          4. Quality Standards
                            - Ensure accurate citations
                            - Maintain academic rigor
                            - Present balanced perspectives
                            - Highlight future research directions\\
                                
                          """),
    expected_output=dedent("""\\ 
                           #{Engaging Title}

                           ## Abstract
                           {Concise overview of the research and key findings}
                           {Give a very detailed description}

                           ## Introduction 
                           {Give a very detailed contextual description of around 800-1000 words}
                           {Context and significance}
                           {Research objectives}

                           ## Methodology
                           {Give a very detailed procedural description of around 850-1000 words}
                           {Search strategy}
                           {Selection criteria}

                           ## Literature Review
                           {Give a very detailed description of around 500-600 words}
                           {Current state of research}
                           {Key findings and breakthroughs}
                           {Emerging trends}

                           ## Analysis
                           {Give a very detailed technical description of around 1400-1600 words}
                           {Critical evaluation}
                           {Cross-study comparisions}
                           {Research gaps}

                           ## Future Directions
                           {Give a very detailed exciting and futuristic description of 600-700 words}
                           {Emerging research opportunities}
                           {Potential applications}
                           {Open questions}

                           ## Conclusions
                           {Give a very detailed and elaborated description of suitable size}
                           {Summary of key findings}
                           {Implications for the field}

                           ## References
                           {APA formatted style}
                           {Properly formatted academic citations}

                           --------
                           Research conducted by Ravi Chandra Vedula
                           Published: {current_date}
                           Last Updated: {current_time}\\
                           """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    save_response_to_file="tmp/{message}.md",                                             
)

# Example usage with academic research request

if __name__=="__main__":
    research_scholar.print_response(
        "Under Water AUV and Gliders application in Indian Ocean Region", 
        stream=True,
)

# Advanced research topics to explore:
"""
Quantum Science & Computing:
1. "Investigate recent breakthroughs in quantum error correction"
2. "Analyze the development of topological quantum computing"
3. "Research quantum machine learning algorithms and applications"
4. "Explore advances in quantum sensing technologies"

Biotechnology & Medicine:
1. "Examine recent developments in mRNA vaccine technology"
2. "Analyze breakthroughs in organoid research"
3. "Investigate advances in precision medicine"
4. "Research developments in neurotechnology"

Materials Science:
1. "Explore recent advances in metamaterials"
2. "Analyze developments in 2D materials beyond graphene"
3. "Research progress in self-healing materials"
4. "Investigate new battery technologies"

Artificial Intelligence:
1. "Examine recent advances in foundation models"
2. "Analyze developments in AI safety research"
3. "Research progress in neuromorphic computing"
4. "Investigate advances in explainable AI"
"""