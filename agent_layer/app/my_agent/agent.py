from google.adk import Agent
from my_agent.prompts.descriptions import AGENT_DESCRIPTIONS
from my_agent.prompts.instructions import AGENT_INSTRUCTIONS

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    description=AGENT_DESCRIPTIONS,
    instruction=AGENT_INSTRUCTIONS
)