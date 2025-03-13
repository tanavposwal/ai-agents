from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.duckduckgo import DuckDuckGo


search_agent = Agent(
    model=Ollama(id="llama3.2"),
    tools=[DuckDuckGo()],
    instructions=[
        "Search through all relevant queries and return the most pertinent information.",
        "Include links to the source of the information format: title 'link'.",
        "And if possible include images in html format. <img src='link'>",
    ],
    # show_tool_calls=True,
    markdown=True,
)
