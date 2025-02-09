import time
import requests
from crewai import Agent, Task, Crew
search_tool = SerperDevTool()

# ---------------------------
# CONFIGURATION
# ---------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"  # Adjust if needed
LLM = None  # Set your LiteLLM instance here

llm = LLM(
    model="ollama/mistral",
    base_url=OLLAMA_URL
)

# ---------------------------
# FUNCTION TO GENERATE AGENT ROLE & DESCRIPTION FROM OLLAMA
# ---------------------------
def fetch_agent_details(role_name):
    """
    Calls a local Ollama instance to generate an agent's role details dynamically.
    """
    prompt = f"Generate a role description and backstory for an AI agent named {role_name}. It should be an expert in its domain."
    
    response = requests.post(OLLAMA_URL, json={"model": "mistral", "prompt": prompt})
    if response.status_code == 200:
        data = response.json()
        generated_text = data.get("response", "No description provided.")
        return generated_text, generated_text  # Return description & backstory
    else:
        return "Default role description", "Default backstory"

def create_agent(role_name, tools=None):
    """
    Creates an AI agent with a dynamically generated role and description.
    """
    description, backstory = fetch_agent_details(role_name)

    return Agent(
        role=role_name,
        goal=f"Perform tasks related to {role_name}.",
        description=description,
        backstory=backstory,
        tools=tools if tools else [search_tool],
        llm=LLM,  # Use LiteLLM instance
        verbose=True
    )

