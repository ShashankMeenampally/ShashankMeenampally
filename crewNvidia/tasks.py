from crewai import Task
from agents import sysadmin_agent

cleanup_task = Task(
    description="""
    Connect to the Linux VM at 192.168.136.128 using SSH.

    Check the disk usage of /tmp.
    If usage is greater than or equal to 80%, clean the files in /tmp.
    Otherwise do nothing.

    Use the cleanup tool available to you.
    """,
    expected_output="A message indicating whether cleanup was executed or skipped based on /tmp usage.",
    agent=sysadmin_agent
)