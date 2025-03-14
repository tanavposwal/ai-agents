from crewai.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchRun


class MyDuckDuckGoTool(BaseTool):
    name: str = "DuckDuckGo Search Tool"
    description: str = "Search the web for a given query."

    def _run(self, query: str) -> str:
        duckduckgo_tool = DuckDuckGoSearchRun()

        response = duckduckgo_tool.invoke(query)

        return response
