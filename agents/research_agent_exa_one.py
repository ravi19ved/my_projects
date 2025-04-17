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

import os
from dotenv import load_dotenv 

load_dotenv() 

os.environ[]