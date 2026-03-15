from utils.schema_validator import validate_schema
from test_data.user_schema import POST_SCHEMA


def test_user_list_schema(api_client):

    response = api_client.send_request(
        "GET",
        "/posts/1"
    )

    validate_schema(response.json(), POST_SCHEMA)