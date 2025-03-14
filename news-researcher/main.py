from crewai import Crew, Process
from agents import researcher, writer
from tasks import researcher_task, writer_task

crew = Crew(
    agents=[researcher, writer],
    tasks=[researcher_task, writer_task],
    process=Process.sequential,
)

result = crew.kickoff()
print(result)
