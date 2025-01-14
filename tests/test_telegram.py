import json
import os

import requests
from dotenv import load_dotenv

from base_classes.test_utility import OutputConsoleResult

load_dotenv()


class TestTelegram:
    def test_telegram_auth(self):
        """
            STEPS:
            3. Execute POST request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "email": os.getenv("PREMIUM_EMAIL"),
            "password": os.getenv("PREMIUM_PASSWORD")
        }
        response = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/telegram/auth",
                                                headers=headers, data=json.dumps(data))
        data = response.json()
        token = data.get("data").get("token")
        assert response.status_code == 200
        assert len(token) > 0
        OutputConsoleResult.print_result(token)

    def test_telegram_auth_email(self):
        """
            STEPS:
            3. Execute POST request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "email": os.getenv("PREMIUM_EMAIL"),
        }
        response = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/telegram/auth/email",
                                                headers=headers, data=json.dumps(data))
        data = response.json()
        result = data.get("exists")
        assert response.status_code == 200
        assert result == True
