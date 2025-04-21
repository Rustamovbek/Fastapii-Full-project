import uuid

def test_register_user(client):
    response = client.post(
        "/auth/",
        json={
            "full_name": "John Doe",
            "email": "JohnDoe@gmail.com",
            "password": "password123",
            "is_active": True,
            "is_admin": False
        }
    )
    assert response.status_code == 201

def test_login_success(client, test_user):
    response = client.post("/auth/token", json={
        "email": test_user["email"],
        "password": test_user["password"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "Bearer"

def test_login_fail_wrong_password(client, test_user):
    response = client.post("/auth/token", json={
        "email": test_user["email"],
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json()["detail"] == "Email or password incorrect"
