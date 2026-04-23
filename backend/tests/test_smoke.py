"""
KunLun Terminal Pro — Smoke Tests
Verifies that the API server boots and all routes are registered.
"""
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "KunLun" in r.json()["name"]


def test_docs_available():
    r = client.get("/docs")
    assert r.status_code == 200


# Each module's route should at minimum return a valid HTTP status
# (will be 500/NotImplemented until services are built out)
@pytest.mark.parametrize("path", [
    "/api/v1/market/indices",
    "/api/v1/market/cloudmap/cn",
    "/api/v1/market/search?q=AAPL",
    "/api/v1/stock/diagnose/AAPL",
    "/api/v1/sentiment/fear-greed",
    "/api/v1/news/latest",
    "/api/v1/strategy/templates",
])
def test_routes_registered(path):
    """Verify route exists (may return 500 until implemented)."""
    r = client.get(path)
    assert r.status_code != 404, f"Route {path} not registered"
