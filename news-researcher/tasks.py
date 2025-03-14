from crewai import Task
from tools import MyDuckDuckGoTool
from agents import researcher, writer

topic = "AI Agents and How it is Changing the World"

researcher_task = Task(
    description=f"""
        The News Research Task involves gathering the most relevant, recent, and credible information about {topic}. The News Researcher Agent will use web search tools and data extraction techniques to compile a structured report containing key insights, historical background, related topics, and diverse perspectives. The goal is to ensure completeness, factual accuracy, and neutrality before the writing process begins.
    """,
    expected_output="""Comprehensive report on this topic.""",
    tools=[MyDuckDuckGoTool()],
    agent=researcher,
)

writer_task = Task(
    description=f"""
        The News Writing Task involves generating a well-structured, fact-based, and engaging blog based on the research report on {topic}. The AI News Writer will use structured inputs (headline, key findings, historical context, related topics) to craft an informative, neutral, and SEO-optimized article.
    """,
    expected_output="""Comprehensive blog on this topic. Expected in markdown format.""",
    agent=writer,
    async_execution=False,
    output_file="markdown/news.md",
)
