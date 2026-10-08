# My Project
## Project Architecture Schema (ABSTRACT)

| Diretório / Arquivo | Tipo | Descrição |
| :--- | :---: | :--- |
| 📁 `my-adk-workspace/` | **Raiz** | Monorepo gerenciado por `uv` |
| ├── 📄 `pyproject.toml` | Config | Configuração global do workspace |
| ├── 📄 `uv.lock` | Lock | Trava de dependências determinística |
| └── 📁 `packages/` | **Pacotes** | Módulos internos do workspace |
|     ├── 🧠 `agent_core/` | **Pacote** | **CÉREBRO:** Regras de negócio e agentes (independente da Web) |
|     │    ├── 📄 `pyproject.toml` | Config | Dependências do `agent_core` |
|     │    └── 📁 `src/agent_core/` | Código | Código-fonte da inteligência |
|     │        ├── 📁 `agents/` | Módulo | Agentes de *...*, *...* e *...* |
|     │        └── 📁 `tools/` | Módulo | Ferramentas executáveis pelos agentes |
|     └── 🚪 `fastapi_app/` | **Pacote** | **PORTA DE ENTRADA:** Interface de rede REST/HTTP |
|         ├── 📄 `pyproject.toml` | Config | Dependências do servidor web |
|         └── 📁 `src/fastapi_app/` | Código | Código-fonte da API |
|             ├── 📄 `main.py` | Entrada | Instância do aplicativo FastAPI |
|             ├── 📁 `api/` | Rotas | Endpoints REST |
|             ├── 📁 `schemas/` | DTOs | Schemas de Request/Response (Pydantic) |
|             └── 📁 `core/` | Infra | Middlewares, Autenticação e Gestão de Sessões |