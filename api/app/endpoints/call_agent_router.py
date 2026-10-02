from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from my_agent.agent import root_agent
from typing import Optional

router = APIRouter(prefix="/agent", tags=["agent"])

# Serviços do ADK
session_service: Optional[InMemorySessionService] = None
runner: Optional[Runner] = None

def get_runner() -> Runner:
    """Lazy initialization do runner."""
    global runner, session_service
    if runner is None:
        session_service = InMemorySessionService()
        runner = Runner(
            agent=root_agent,
            app_name="my_app",
            session_service=session_service,
        )
    return runner

class AgentRequest(BaseModel):
    message: str
    session_id: str = "default"
    user_id: str = "default_user"

class AgentResponse(BaseModel):
    response: str

@router.post("", response_model=AgentResponse)
async def call_agent(request: AgentRequest):
    """Chama o agente ADK com uma mensagem."""
    try:
        runner_instance = get_runner()
        
        # Criar Content com Part correto
        user_message = types.Content(
            role="user",
            parts=[types.Part.from_text(request.message)]  # ← Usar Part.from_text
        )
        
        events = runner_instance.run_async(
            user_id=request.user_id,
            session_id=request.session_id,
            new_message=user_message,
        )
        
        # Iterar sobre os eventos
        final_response = None
        async for event in events:
            if hasattr(event, 'final_response') and event.final_response:
                final_response = event.final_response
        
        response_text = final_response or "Sem resposta do agente"
        return AgentResponse(response=response_text)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no agente: {str(e)}")