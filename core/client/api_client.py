import requests
from core.config.config import Config


class APIClient:

    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {
            "x-api-key": Config.API_KEY,
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers
        )

    def post(self, endpoint, payload):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            headers=self.headers
        )