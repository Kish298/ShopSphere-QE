from core.client.api_client import APIClient

client = APIClient()


def test_get_users():
    response = client.get("/users?page=2")

    assert response.status_code == 200
    assert "data" in response.json()