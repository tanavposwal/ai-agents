from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

load_dotenv()

llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")

# agents do tasks
info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic",
    backstory="""
        Your love to know information. People love and hate you for it. YOu win most of the quizzes at your local pub.
    """,
    llm=llm,
)

task1 = Task(
    description="Tell me all about the blue-ringed octopus.",
    expected_output="Give me a quick summary and then also give me a seven bullet point describing this. Write in markdown and do not add the triple tick marks at the beginning or end of the file.",
    output_file="markdown/octopus.md",
    agent=info_agent,
)

crew = Crew(
    agents=[info_agent],
    tasks=[task1],
)

result = crew.kickoff()
