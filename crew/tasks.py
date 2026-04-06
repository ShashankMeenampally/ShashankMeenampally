from crewai import Task
from agents import sysadmin_agent

cleanup_task = Task(
    description="""
    Check disk usage on server 192.168.136.128 using check_disk tool.
    
    If usage is 60% or more:
        - Use cleanup tool to delete all files in /tmp
        - Check disk usage again
    
    Report: "Before: X%, After: Y%"
    """,
    expected_output="Disk usage before and after cleanup",
    agent=sysadmin_agent
)