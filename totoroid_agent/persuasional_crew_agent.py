from crewai import Agent, Task, Crew

llm = LLM(
    model="ollama/mistral",
    base_url="http://localhost:11434"
)

# Agent 1: Idea Generator (Perspective A)
idea_generator = Agent(
    role="Creative Thinker",
    goal="Come up with innovative ideas from a futuristic perspective.",
    description="You are a visionary who explores creative possibilities for solving problems.",
    backstory="A futurist known for predicting technological trends and their impact on society.",
        llm=llm,  # Use LiteLLM

    verbose=True
)

# Agent 2: Solution Generator (Perspective B)
solution_generator = Agent(
    role="Practical Engineer",
    goal="Develop realistic and practical solutions based on today's technology.",
    description="You are an expert in engineering who creates feasible solutions.",
    backstory="An experienced engineer who prioritizes practicality over speculation.",
        llm=llm,  # Use LiteLLM

    verbose=True
)

# Agent 3: Discriminator (Evaluator)
discriminator = Agent(
    role="Evaluator",
    goal="Select the best idea based on feasibility and impact.",
    description="You analyze the suggestions and choose the most effective solution.",
    backstory="A seasoned decision-maker with experience in risk assessment and implementation.",
        llm=llm,  # Use LiteLLM

    verbose=True
)

# Tasks for Agents
task_idea = Task(
    description="Generate three futuristic ideas to solve climate change.",
    agent=idea_generator,
    expected_output="A list of three innovative solutions with futuristic approaches."
)

task_solution = Task(
    description="Generate three practical solutions to solve climate change.",
    agent=solution_generator,
    expected_output="A list of three solutions that can be implemented today."
)

task_evaluation = Task(
    description="Compare the ideas from the Creative Thinker and the Practical Engineer. Select the best approach and justify your reasoning.",
    agent=discriminator,
    context=[task_idea.output, task_solution.output],
    expected_output="A final decision on the best idea with an explanation."
)

# Crew Setup
crew = Crew(
    agents=[idea_generator, solution_generator, discriminator],
    tasks=[task_idea, task_solution, task_evaluation]
)

# Run the Crew
result = crew.kickoff()
print("\nFinal Decision:", result)
