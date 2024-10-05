def test_create_user(client):
    response = client.post("/users/", json={"username": "johndoe", "email": "johndoe@example.com"})
    assert response.status_code == 200
    assert response.json()["username"] == "johndoe"
