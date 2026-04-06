from crewai import Agent, LLM
from tools.cleanup_tool import CleanupTmpTool
import os

llm = LLM(
    #model="openai/gpt-4o-mini",
    #model="google/gemma-3n-e2b-it:free",
    model="GPT-4o-mini",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY")
)

cleanup_tool = CleanupTmpTool()

sysadmin_agent = Agent(
    role="Linux System Maintenance Engineer",
    goal="Maintain server hygiene and prevent disk space issues",
    backstory=(
        "You are a veteran DevOps engineer specialized in Linux automation."
    ),
    tools=[cleanup_tool],
    llm=llm,
    verbose=True
)