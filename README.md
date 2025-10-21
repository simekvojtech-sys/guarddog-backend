# Guard Dog API (FastAPI)

Quick-start backend to support the Guard Dog frontend.

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```
Visit http://127.0.0.1:8080/docs
