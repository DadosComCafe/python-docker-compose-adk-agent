import asyncio
import logging
import os
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.agents import Agent
from agent_core.prompts.descriptions.agent_descriptions import security_guard_descriptions
from agent_core.prompts.instructions.agent_instructions import security_guard_instructions
from google.genai import types

security_guard_agent = Agent(
    model='gemini-3.8-flash',
    name='security_guard_agent',
    description=security_guard_descriptions,
    instruction=security_guard_instructions,
)

APP_NAME = "security_guard_app"
USER_ID = "test_user"

os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["OTEL_TRACES_EXPORTER"] = "none"
os.environ["OTEL_METRICS_EXPORTER"] = "none"
logging.getLogger("opentelemetry").setLevel(logging.CRITICAL)

async def main():
    session_service = InMemorySessionService()
    
    runner = Runner(
        agent=security_guard_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state={"initial_key": "initial_value"}#opcional, dar uma estudada nisso
    )
    print(f"Sessão criada: {session.id}")

    content = types.Content(role='user', parts=[types.Part(text="Qual é a sua função?")])

    final_text = None
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session.id,
        new_message=content
    ):
        if event.is_final_response() and event.content is not None:
            if event.content.parts:
                final_text = event.content.parts[0].text
                break

    print(f"Resposta do agente: {final_text}")

if __name__ == "__main__":
    asyncio.run(main())