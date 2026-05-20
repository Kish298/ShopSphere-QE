import pytest

from core.client.api_client import APIClient
from test_data.user_payloads import CREATE_USER

client = APIClient()

@pytest.mark.api
@pytest.mark.smoke
def test_get_posts(api_client):

    response = api_client.send_request(
        "GET",
        "/posts"
    )

    assert response.status_code == 200