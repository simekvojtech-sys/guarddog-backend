from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from . import db

app = FastAPI(title="Guard Dog API", version="0.1.0")

origins = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Company(BaseModel):
  ticker: str
  name: str | None = None
  cik: str | None = None

@app.get("/api/health")
def health():
    return {"ok": True, "service": "guarddog-api", "version": "0.1.0"}

@app.get("/api/companies/{ticker}", response_model=Company)
def get_company(ticker: str):
    # TODO: map ticker->CIK, pull profile from DB or external
    t = ticker.upper()
    return Company(ticker=t, name=f"{t} Holdings, Inc.", cik=None)

@app.get("/api/companies/{ticker}/filings")
def filings(ticker: str, form: str | None = None, limit: int = 20):
    # TODO: fetch from DB; this is stubbed
    sample = [
        {"form": "10-Q", "filed_at": "2025-10-29", "title": "Quarterly Report", "accession_no": "0000-25-123", "sec_url": "https://www.sec.gov/"},
        {"form": "8-K", "filed_at": "2025-09-30", "title": "Current Report", "accession_no": "0000-25-111", "sec_url": "https://www.sec.gov/"}
    ]
    if form:
        sample = [x for x in sample if x["form"] == form]
    return sample[:limit]

@app.get("/api/companies/{ticker}/events")
def events(ticker: str, from_: str | None = None, to: str | None = None):
    # TODO: fetch from DB; this is stubbed
    return [
        {"date": "2025-12-05", "type": "Shareholder Meeting", "title": "Annual Meeting", "source_url": None, "all_day": True},
        {"date": "2026-02-03", "type": "Earnings", "title": "Q2 FY26 Earnings (proj)", "source_url": None, "all_day": True},
    ]

@app.get("/api/reports")
def reports(period: str = "week"):
    # TODO: return compiled user reports from DB
    return [{"id": "rpt_demo", "period_start": "2025-10-20", "period_end": "2025-10-27", "items": []}]
@app.get("/api/db/ping")
def db_ping():
    """Verify API can connect to Postgres (Neon)."""
    return db.ping()
