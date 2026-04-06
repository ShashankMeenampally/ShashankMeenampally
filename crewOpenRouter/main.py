import os
from dotenv import load_dotenv

load_dotenv()   # this loads C:\Data\OUTSKILL\.env

from crewai import Crew, Process
from agents import sysadmin_agent
from tasks import cleanup_task

crew = Crew(
    agents=[sysadmin_agent],
    tasks=[cleanup_task],
    process=Process.sequential
)

result = crew.kickoff(
    inputs={"host": "192.168.136.128"}
)

print(result)