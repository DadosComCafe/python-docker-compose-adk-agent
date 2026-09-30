# run.py
import sys
from pathlib import Path

# Adicionar ambos os módulos ao path
agent_layer_path = Path(__file__).parent / "agent_layer" / "app"
api_path = Path(__file__).parent / "api" / "app"

sys.path.insert(0, str(agent_layer_path))
sys.path.insert(0, str(api_path))

# Agora importar o app FastAPI
from main import app  # vem de api/app/main.py
print("ok0")
if __name__ == "__main__":
    import uvicorn
    print("ok")
    uvicorn.run(app, host="0.0.0.0", port=8000)