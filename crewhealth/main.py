import os
from crewai import Crew, Process, LLM
from dotenv import load_dotenv
from agent import create_agent
from tasks import create_task
import sys


# Fix Windows encoding
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv()

# -------------------------------
# LLM CONFIGURATION
# -------------------------------
llm = LLM(
    model="stepfun-ai/step-3.5-flash",
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ.get("NVIDIA_API_KEY")
)

# -------------------------------
# CREATE AGENT AND TASK
# -------------------------------
agent = create_agent(llm)
task = create_task(agent)

# -------------------------------
# CREATE AND RUN CREW
# -------------------------------
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential
)

print("\n" + "="*50)
print("Starting CrewAI Monitoring System")
print("="*50 + "\n")

result = crew.kickoff()

print("\n" + "="*50)
print("RESULT:")
print("="*50)
print(result)