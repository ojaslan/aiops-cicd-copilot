from strands import Agent
from strands.models import BedrockModel
import os


model = BedrockModel(
    model_id="apac.amazon.nova-lite-v1:0",
    region_name=os.getenv("AWS_REGION", "ap-south-1")
)


SYSTEM_PROMPT = """
You are an expert AIOps and DevOps engineer.

Your job is to analyze CI/CD pipeline failures.

When given CI/CD logs:

1. Identify the failure.
2. Determine the likely root cause.
3. Explain the failure in simple technical language.
4. Identify the failed stage.
5. Provide the exact remediation steps.
6. Mention useful commands when applicable.
7. Do not invent information that is not present in the logs.

Return your response using this structure:

## Failure Summary
## Failed Stage
## Root Cause
## Evidence
## Recommended Fix
## Verification Steps
"""


agent = Agent(
    model=model,
    system_prompt=SYSTEM_PROMPT
)


def analyze_logs(logs: str) -> str:
    prompt = f"""
Analyze the following CI/CD pipeline logs.

CI/CD LOGS:
----------------
{logs}
----------------

Provide the complete AIOps analysis.
"""

    response = agent(prompt)

    return str(response)