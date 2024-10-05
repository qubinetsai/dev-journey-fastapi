import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils.auth import SessionLocal


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture(scope="module")
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
