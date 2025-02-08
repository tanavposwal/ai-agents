from phi.agent import Agent
from dotenv import load_dotenv
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.playground import Playground, serve_playground_app

load_dotenv()


web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    storage=SqlAgentStorage(table_name="web_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
    instructions=["Always include sources."],
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        )
    ],
    storage=SqlAgentStorage(table_name="finance_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
    instructions=["Use tables to display data."],
)

team_agent = Agent(
    team=[web_agent, finance_agent],
    instructions=["Always include sources.", "Use tables to display data."],
    model=Groq(id="llama-3.3-70b-versatile"),
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[team_agent, finance_agent, web_agent]).get_app()

# team_agent.print_response(
#     "Get analyst recommendations and the latest news for NVDA and from that tell me to buy or sell that and reson in table format and numbers."
# )

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
