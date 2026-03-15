import requests
from core.config.config import Config
from core.logger.logger import get_logger

logger = get_logger(__name__)


class APIClient:

    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {
            "Content-Type": "application/json"
        }

    def send_request(self, method, endpoint, payload=None):

        url = f"{self.base_url}{endpoint}"

        logger.info(f"{method} Request → {url}")

        response = requests.request(
            method=method,
            url=url,
            json=payload,
            headers=self.headers
        )

        logger.info(f"Response Status → {response.status_code}")

        return response