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
from database import Base
from main import get_db
from models.user import User

# Parolni hash qilish funksiyasi
def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

# Test uchun vaqtinchalik database
TEST_DB_FILE = tempfile.NamedTemporaryFile(delete=False)
TEST_SQLALCHEMY_DATABASE_URL = f"sqlite:///{TEST_DB_FILE.name}"

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DB override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Database setup/teardown
@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    yield
    Base.metadata.drop_all(bind=engine)
    TEST_DB_FILE.close()
    os.unlink(TEST_DB_FILE.name)

# Test client
@pytest.fixture
def client():
    return TestClient(app)

# Test user yaratish
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
