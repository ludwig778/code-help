def test_ping(unauthorized_client):
    response = unauthorized_client.get("/api/ping")

    assert response.json() == {"status": "ok"}
    assert response.status_code == 200
