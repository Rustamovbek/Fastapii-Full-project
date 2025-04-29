# tests/conftest.py
import os
import tempfile
import pytest
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
import uuid
from main import app
from core.database import Base
from core.db_conf import get_db
from models.user import User

def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

TEST_DB_FILE = tempfile.NamedTemporaryFile(delete=False)
TEST_SQLALCHEMY_DATABASE_URL = f"sqlite:///{TEST_DB_FILE.name}"

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    yield
    Base.metadata.drop_all(bind=engine)
    TEST_DB_FILE.close()
    os.unlink(TEST_DB_FILE.name)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def test_user():
    db = TestingSessionLocal()
    email = f"{uuid.uuid4()}@example.com"
    hashed_pw = get_password_hash("password123")
    user = User(
        full_name="John Doe",
        email=email,
        hashed_password=hashed_pw,
        is_active=True,
        is_admin=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "email": user.email,
        "password": "password123"
    }