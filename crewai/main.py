from crewai import Agent, Task, Crew

# Define an agent for handling general queries (e.g., sales inquiries)
sales_agent = Agent(
    role="Sales Agent",
    goal="Answer product pricing and offer inquiries",
    backstory="""
        You are friendly and efficient. When a customer asks about pricing or offers,
        you provide concise and accurate details.
    """,
    llm="ollama/llama3.2",  # Replace with your desired local model identifier
)

# Define another agent for handling technical support queries
tech_support_agent = Agent(
    role="Tech Support Agent",
    goal="Assist customers with technical issues",
    backstory="""
        You are knowledgeable about troubleshooting products.
        Answer technical questions with clear instructions.
    """,
    llm="ollama/llama3.2",  # You can use the same or another model as needed
)

# Create tasks for each agent
task_sales = Task(
    description="A customer asks, 'What is the price of product X?'",
    expected_output="Provide the pricing details of product X.",
    agent=sales_agent,
)

task_tech = Task(
    description="A customer says, 'I can't connect my device to the internet.'",
    expected_output="Offer technical support instructions for connectivity issues.",
    agent=tech_support_agent,
)

# Set up a Crew to manage these agents and their tasks
crew = Crew(
    agents=[sales_agent, tech_support_agent],
    tasks=[task_sales, task_tech],
    verbose=True,  # This enables more detailed logging of the process
)

# Kick off the crew with some input parameters if required
result = crew.kickoff(inputs={"customer_query": "What is the price of product X?"})
print(result)
