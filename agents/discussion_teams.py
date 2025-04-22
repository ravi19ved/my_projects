import asyncio
from textwrap import dedent

from agno.agent import Agent 
from agno.models.openai import OpenAIChat 
from agno.team.team import Team 
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.arxiv import ArxivTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.hackernews import HackerNewsTools


# API Access setup
import os
from dotenv import load_dotenv 

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Agents and Agents team creation

reddit_researcher = Agent(
    name = "Reddit Researcher",
    role = "Research a topic on Reddit",
    model = OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    add_name_to_instructions=True,
    instructions=dedent("""\
                        You are a Reddit researcher.
                        You will be given a topic to research on Reddit.
                        You will need to find the most relevant posts on Reddit.
                        """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

hackernews_researcher = Agent(
    name = "Hacker News Researcher",
    role = "Research the topic on HackerNews and give the best results",
    model = OpenAIChat(id="gpt-4o"),
    tools = [HackerNewsTools()],
    add_name_to_instructions=True, 
    instructions=dedent("""\
                        You are a HackerNews researcher.
                        You will be given a topic to research on HackerNews.
                        You will need to find the most relevant posts on HackerNews.
                        """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

academic_paper_researcher = Agent(
    name = "Academic Paper Researcher",
    role = "Research academic papers and scholarly content",
    model = OpenAIChat("gpt-4o"),
    tools = [GoogleSearchTools(), ArxivTools()],
    add_name_to_instructions=True,
    instructions=("""\
                  You are an academic paper researcher.
                  You will be given a topic to research in academic literature.
                  You will need to find relevant scholarly articles, papers, and academic discussions.
                  Focus on peer-reviewed content and citations from reputable sources.
                  Proide brief summaries of key findings and methodologies.
                  """),
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    markdown=True,    
)

twitter_researcher = Agent(
    name = "Twitter Researcher",
    model = OpenAIChat(id="gpt-4o"),
    role = "Research trending discussions and real-time updates on Twitter/X platform.",
    tools=[DuckDuckGoTools()],
    add_name_to_instructions=True,
    instructions=dedent("""\
                        You are a Twitter/X researcher.
                        You will be given a topic to research on Twitter/X.
                        You will need to find trending discussions, influential voices, and real time updates. 
                        Focus on verified accounts and credible sources when possible.
                        Track relevant hashtags and onging conversations.
                        """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
)

agent_team = Team(
    name = "Discussion Team",
    mode="collaborate",
    model=OpenAIChat("gpt-4o"),
    members=[
        reddit_researcher,
        hackernews_researcher,
        academic_paper_researcher,
        twitter_researcher,
    ],
    instructions=[
        "You are a discussion master.",
        "You have to stop the discussions when you think the team has reached a consensus.",
        ],
        success_criteria="The team has reached a consensus.",
        show_tool_calls=True,
        send_team_context_to_members=True,
        update_team_context = True,
        debug_mode=True,
        markdown=True,
        show_members_responses=True,
)

if __name__=="__main__":
    asyncio.run(
        agent_team.print_response(
            message="Start the discussion on the topic: 'What is the best way to learn to code?'",
            stream=True,
            stream_intermediate_steps=True,
        )
    )