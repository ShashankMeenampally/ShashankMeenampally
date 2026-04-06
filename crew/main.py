import os
from dotenv import load_dotenv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

load_dotenv()

# Debug: Check if API key is loaded
print(f"API Key loaded: {'Yes' if os.getenv('TOKEN') else 'No'}")

from crewai import Crew, Process
from agents import sysadmin_agent
from tasks import cleanup_task

crew = Crew(
    agents=[sysadmin_agent],
    tasks=[cleanup_task],
    process=Process.sequential,
    verbose=True  # Enable crew-level verbosity
)

result = crew.kickoff(
    inputs={"host": "192.168.136.128"}
)

print("\n" + "="*50)
print("FINAL RESULT:")
print("="*50)
print(result)