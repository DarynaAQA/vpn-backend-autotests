import os

import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn
from base_classes.test_utility import OutputConsoleResult
from methods_for_routes.base_methods import AvailabilityRoutes

load_dotenv()


class TestOtherRoutes:

    def test_get_status_json(self):
        base_methods = AvailabilityRoutes()
        DataIn.token = base_methods.authenticate_premium_user()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        get_status_json = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/status.json",
                                        headers=headers)
        status_json = get_status_json.json()
        data = status_json.get("service")
        assert get_status_json.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)
