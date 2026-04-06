import os
from crewai import Agent, LLM
from tools.cleanup_tool import check_disk, cleanup

llm = LLM(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ.get("NVIDIA_API_KEY"),
    model="stepfun-ai/step-3.5-flash",
)

sysadmin_agent = Agent(
    role="System Admin",
    goal="Keep disk usage under 60%",
    backstory="You monitor disk space and clean /tmp when needed.",
    tools=[check_disk, cleanup],
    llm=llm,
    verbose=True,
)