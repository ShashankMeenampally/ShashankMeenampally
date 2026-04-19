from crewai import Task

def create_task(agent):
    """Create and return the monitoring task"""
    
    task = Task(
        description="Check /tmp usage on server and report if above 60%",
        expected_output="OK or WARNING with percentage",
        agent=agent
    )
    
    return task