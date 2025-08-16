import os
import sys
from fastapi.testclient import TestClient

os.environ["DATABASE_URL"] = "sqlite:///:memory:"
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app.main import app

client = TestClient(app)


def test_holdings():
    r = client.get("/api/holdings")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_analytics():
    r = client.get("/api/analytics")
    assert r.status_code == 200
    data = r.json()
    assert "sharpe" in data and "correlation" in data


def test_optimization():
    r = client.get("/api/optimization")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert data and "risk" in data[0] and "return" in data[0]
