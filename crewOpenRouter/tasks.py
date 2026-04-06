from crewai import Task
from agents import sysadmin_agent

cleanup_task = Task(
    description="""
    Connect to the Linux VM at 192.168.136.128 using SSH.
    The username is admin.

    Clean the /tmp directory to remove temporary files.
    Use the cleanup tool to perform the operation.
    """,
    expected_output="Confirmation that /tmp directory was cleaned on 192.168.136.128.",
    agent=sysadmin_agent
)