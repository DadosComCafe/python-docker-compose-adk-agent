# The Security Guard
Este projeto é o desenvolvimento de um agente (e o sistema para disponibilizá-lo) que realizará o processo de validação dos dados, antes que estes dados sejam ingeridos através do Airflow (hipotético). Portanto, com este agente o usuário irá garantir que a ingestão ocorrerá com sucesso, e os dados do .csv ou do .xlsx. Desta forma, uma vez que os arquivos passarem pelo agente, há maiores garantias de que todo o processo de ingestão ocorrerá sem falhas de formatação, tipagem ou não conformidade com as tabelas destinos, uma vez que esta validação já terá sido realizada.

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