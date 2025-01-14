import json
import os

import pytest
import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn

load_dotenv()


class TestVotes:
    @pytest.mark.parametrize("app", DataIn.uuid_apps)
    def test_vote_like(self, app):
        headers = {
            "UUID-APP": app.get("uuid"),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "type": 1
        }
        response = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("PRE_PROD_DOMAIN")}/v1/votes",
                                    headers=headers, data=json.dumps(data))
        response_data = response.json()
        result = response_data.get("success")
        assert response.status_code == 200
        assert result == True

    @pytest.mark.parametrize("app", DataIn.uuid_apps)
    def test_vote_dislike(self, app):
        headers = {
            "UUID-APP": app.get("uuid"),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "type": 2
        }
        response = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v1/votes",
                                    headers=headers, data=json.dumps(data))
        response_data = response.json()
        result = response_data.get("success")
        assert response.status_code == 200
        assert result == True
