from agno.agent import Agent 
from agno.models.openai import OpenAIChat 
from agno.models.groq import Groq 
from agno.playground import Playground, serve_playground_app 
from agno.storage.agent.sqlite import SqliteAgentStorage 
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.arxiv import 
from agno.tools.yfinance import YFinanceTools 

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent_storage: str = "tmp/agents.db"

web_agent = Agent(
    name = "Web Agent", 
    model = OpenAIChat(id= "gpt-4o"),
    tools = [DuckDuckGoTools()],
    instructions = ["Always include the sources"],

    # Store the agent sessions in a sqlite database
    storage = SqliteAgentStorage(table_name="web_agent", db_file = agent_storage),

    #Adds the current date and time to the instructions
    add_datetime_to_instructions=True, 

    # Adds the history of the conversation to the messages
    add_history_to_messages=True,

    # Number of history responses to add to the message
    num_history_responses= 5, 

    # Adds markdown formating to the messages
    markdown=True,
    
)

finance_agent = Agent(
    name = "Finance Agent",
    model = OpenAIChat(id="gpt-4o"),
    tools= [YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions = ["Always use tables to display data."],
    storage = SqliteAgentStorage(table_name="finance_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

research_agent = Agent(
    name = "Research Agent",
    model = OpenAIChat(id="gpt-4o"),
    tools= [DuckDuckGoTools(search=True, fixed_max_results=10, news=True)],
    instructions = ["Prefer scientific publications and research publications during the search.",
                    "The writing style should match high impact factor journals like science, nature, JGR editorial standards",
                    "Generate tables when ever necessary to display data to be incorporated into scientific publication"],
    storage = SqliteAgentStorage(table_name="research_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    expected_output="Include citations and references in APA style", 
    structured_outputs=True,
    save_response_to_file="my_test_file.txt",
    markdown=True,
)

app = Playground(agents=[web_agent, finance_agent, research_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
