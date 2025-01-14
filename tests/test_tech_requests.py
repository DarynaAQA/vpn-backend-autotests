import os

import requests
from dotenv import load_dotenv

from base_classes.test_utility import OutputConsoleResult

load_dotenv()


class TestTechRequests:
    def test_tech_nodes_ip(self):
        headers = {
            "Basic": os.getenv("PRE_PROD_BASIC_TECH_TOKEN"),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("PRE_PROD_DOMAIN")}/tech/nodes/ip",
                                             headers=headers)
        response_data = response.text
        assert response.status_code == 200
        assert len(response_data) > 0
        OutputConsoleResult.print_result(response_data)

    def test_tech_nodes_monitoring(self):
        headers = {
            "Basic": os.getenv("PRE_PROD_BASIC_TECH_TOKEN"),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("PRE_PROD_DOMAIN")}/tech/nodes/monitoring",
                                             headers=headers)
        response_data = response.text
        assert response.status_code == 200
        assert len(response_data) > 0
        OutputConsoleResult.print_result(response_data)

    def test_logging_instals_v1(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v1/logging/installs"
                                    "?offer=2&campaign=2&source=1&session_id=3", headers=headers)
        response_data = response.json()
        result = response_data.get("data").get("success")
        assert response.status_code == 200
        assert result == True