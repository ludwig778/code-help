def test_get_logged_user_info(client):
    response = client.get("/api/v1/users/me")

    assert response.json() == {
        "username": "user_2",
        "email": "user_2@example.com",
        "is_active": True,
        "is_superuser": False,
    }
    assert response.status_code == 200
