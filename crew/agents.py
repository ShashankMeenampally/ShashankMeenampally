import os
from crewai import Agent, LLM
from tools.cleanup_tool import cleanup_tmp_directory

llm = LLM(
    # model="gpt-4o",
    # base_url="https://labs.pluralsight.com/labs-ai-proxy/rest/openai/chatgpt-4o/v1",
    # api_key=os.getenv("TOKEN"),
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ.get("NVIDIA_API_KEY"),
    model="stepfun-ai/step-3.5-flash",
    timeout=60,  # Add timeout
    max_retries=3,  # Add retries
)

sysadmin_agent = Agent(
    role="Linux System Maintenance Engineer",
    goal="Maintain server hygiene and prevent disk space issues",
    backstory=(
        "You are an experienced DevOps engineer who automates "
        "server maintenance and prevents system failures."
    ),
    tools=[cleanup_tmp_directory],
    llm=llm,
    verbose=True,
    max_iter=3,  # Limit iterations to prevent loops
)