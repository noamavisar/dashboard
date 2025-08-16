from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from . import models, schemas, ibkr
from .analytics import compute_metrics
from .optimization import efficient_frontier_points

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/portfolio")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/holdings", response_model=list[schemas.Holding])
def read_holdings():
    """Return current portfolio holdings."""
    return ibkr.get_holdings()

@app.websocket("/ws/updates")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # Placeholder for pushing real-time updates
    await websocket.send_text("update")
    await websocket.close()


@app.get("/api/analytics", response_model=schemas.Analytics)
def analytics():
    """Return basic risk metrics and correlations."""
    return compute_metrics()


@app.get("/api/optimization", response_model=list[schemas.FrontierPoint])
def optimization():
    """Return efficient frontier points."""
    return efficient_frontier_points()
