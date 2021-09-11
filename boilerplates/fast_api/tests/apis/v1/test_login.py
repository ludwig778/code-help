def test_login(unauthorized_client):
    client = unauthorized_client

    response = client.post(
        "/api/v1/login/", data={"username": "user_1", "password": "secret_1"}
    )

    assert response.status_code == 200
    assert response.json().get("access_token")


def test_failed_login(unauthorized_client):
    client = unauthorized_client

    response = client.post(
        "/api/v1/login/", data={"username": "user_1", "password": "wrontsecret"}
    )

    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_access_token(unauthorized_client):
    client = unauthorized_client

    response = client.post(
        "/api/v1/login/", data={"username": "user_1", "password": "secret_1"}
    )
    access_token = response.json().get("access_token")

    client.headers.update({"Authorization": f"Bearer {access_token}"})

    response = client.get("/api/v1/users/me/")

    assert response.json() == {
        "username": "user_1",
        "email": "user_1@example.com",
        "is_active": True,
        "is_superuser": True,
    }
    assert response.status_code == 200


def test_disabled_user_token(unauthorized_client):
    client = unauthorized_client

    response = client.post(
        "/api/v1/login/", data={"username": "user_3", "password": "secret_3"}
    )
    access_token = response.json().get("access_token")

    client.headers.update({"Authorization": f"Bearer {access_token}"})

    response = client.get("/api/v1/users/me/")

    assert response.json() == {"detail": "Inactive user"}
    assert response.status_code == 400


def test_wrong_access_token(unauthorized_client):
    client = unauthorized_client

    client.headers.update({"Authorization": "Bearer wrong_token"})

    response = client.get("/api/v1/users/me/")

    assert response.json() == {"detail": "Could not validate credentials"}
    assert response.status_code == 401
