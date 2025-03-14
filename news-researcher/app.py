import streamlit as st
from crewai import Crew, Process
from agents import researcher, writer
from tasks import create_researcher_task, create_writer_task
import os

# Streamlit UI
st.title("News Researcher")

# Input for topic
topic = st.text_input("Enter a topic for news research:")

if st.button("Generate News"):
    if topic:
        # Create the tasks with the provided topic
        researcher_task = create_researcher_task(topic)
        writer_task = create_writer_task(topic)

        # Create the Crew
        crew = Crew(
            agents=[researcher, writer],
            tasks=[researcher_task, writer_task],
            process=Process.sequential,
        )

        # Run the Crew
        result = crew.kickoff()

        if result:  # Check if the Crew completed successfully
            st.success("News generation completed!")

            # Display the generated news.md file
            if os.path.exists("markdown/news.md"):
                with open("markdown/news.md", "r") as file:
                    news_content = file.read()
                st.markdown(news_content)
            else:
                st.error("The news.md file was not found.")
        else:
            st.warning(
                "The Crew did not complete successfully. Please check the logs for errors."
            )
    else:
        st.warning("Please enter a topic.")
