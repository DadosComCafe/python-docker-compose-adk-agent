# My Project

## Project Architecture Schema
| Service  | Tecnology | Framework / Extension |
| -------- | ---------- | -------------------- |
| agent   | Python     | ADK                  |
| api      | Python     | FastAPI              |
| database | PostgreSQL | pgvector             |

## How To Run
1 - git clone

2 - uv sync

3 - uv run --package app uvicorn api.app.main:app --reload --port 8001