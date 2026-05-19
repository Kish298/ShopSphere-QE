import pytest

from test_data.user_payloads import CREATE_USER
from utils.assertions import assert_status

@pytest.mark.api
@pytest.mark.regression
def test_create_post(api_client):

    response = api_client.send_request(
        "POST",
        "/posts",
        payload=CREATE_USER
    )

    assert_status(response, 201)

    data = response.json()

    assert data["title"] == CREATE_USER["title"]