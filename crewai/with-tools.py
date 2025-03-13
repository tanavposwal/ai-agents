from crewai import Agent, Task, Crew, LLM, Process
from crewai.tools import tool


@tool("Calculate")
def calculate(equation: str):
    """Useful for solving math equation"""

    return eval(equation)


# equation - 4+2*-5/2+6/4
llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")

print("## Welcome to the Math Whiz")
math_input = input("What is your math equation: ")

math_agent = Agent(
    role="Math Magician",
    goal="You are able to evaluate any math expression",
    backstory="""
        YOU ARE A MATH WHIZ.
    """,
    llm=llm,
    tools=[calculate],
    verbose=True,
)

writer = Agent(
    role="Writer",
    goal="Craft compelling explanation based from result of math equations.",
    backstory="""
        You are a renowned content strategist, known for your insightful and engaging articles. You transform complex concepts into compelling narratives.
    """,
    llm=llm,
    verbose=True,
)

task1 = Task(
    description=f"{math_input}",
    expected_output="""
        Give full details in bullet points.
    """,
    agent=math_agent,
)

task2 = Task(
    description="Using the insights provided, explain in great detail how the equations and results were found.",
    expected_output="""
        Explain in great detail and save in markdown. Do not add the triple tick marks at the beginning or end of the file. Also don't say what type it is in the first line.
    """,
    output_file="markdown/math.md",
    agent=writer,
)

crew = Crew(
    agents=[math_agent, writer],
    tasks=[task1, task2],
    process=Process.sequential,
    verbose=True,
)

result = crew.kickoff()
print(result)
