import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
FRONTEND_DIR = BASE_DIR / "Frontend"

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    env_path = BASE_DIR / "Backend" / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"\''))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import pages, api

app = FastAPI(title="LeadForge AI")

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR / "static")), name="static")
app.include_router(pages.router)
app.include_router(api.router)
