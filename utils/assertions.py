def assert_status(response, expected_code):
    assert response.status_code == expected_code