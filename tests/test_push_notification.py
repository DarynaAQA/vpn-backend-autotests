import requests
from dotenv import load_dotenv
import os
import datetime
from base_classes.test_utility import OutputConsoleResult

load_dotenv()


class TestPushNotification:

    def test_add_new_token_device(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "Authorization": f"Bearer {os.getenv("ADMIN_JWT_TOKEN")}",
            "UUID-APP": "417d6c71-0a98-4215-8c97-bba837b15161"
        }
        add_new_token = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/device-token/add",
                                      headers=headers, data={
                "device_token": "test_2",
                "locale": "ru",
                "geo_tag": "tr"
            })
        assert add_new_token.status_code == 201

    def test_device_token_refresh(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "UUID-APP": "417d6c71-0a98-4215-8c97-bba837b15161"
        }
        current_time = datetime.datetime.now()
        refresh_token = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/device-token/refresh",
                                      headers=headers, data={
                "old_token": "test_2",
                "new_token": f"new-test-{current_time}",
                "locale": "en",
                "geo_tag": "en"
            })
        refresh_token_json = refresh_token.json()
        assert refresh_token.status_code == 201
        assert len(refresh_token_json) > 0
        OutputConsoleResult.print_result(refresh_token_json)
