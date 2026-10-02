from fastapi import FastAPI
from .endpoints import health_router, call_agent_router

app = FastAPI(
    title="My Agent API",
    description="API para chamar o agente ADK",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(call_agent_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}