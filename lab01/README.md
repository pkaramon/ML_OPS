# Lab 1

Iris classifier served with FastAPI.

```bash
uv sync
uv run python training.py          # trains and saves models/model.joblib
uv run uvicorn app:app --reload    # http://localhost:8000
uv run pytest tests -rP
docker compose up
```
