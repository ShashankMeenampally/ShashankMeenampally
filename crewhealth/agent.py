from crewai import Agent
from tools import DiskTool

def create_agent(llm):
    """Create and return the monitoring agent"""
    
    agent = Agent(
        role="Monitor",
        goal="Check /tmp usage",
        backstory="Linux admin",
        tools=[DiskTool()],
        llm=llm,
        verbose=True
    )
    
    return agent