import os
import time

import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn
from base_classes.test_utility import OutputConsoleResult
from methods_for_routes.base_methods import AvailabilityRoutes
from methods_for_routes.decrypt_payload import DecryptData

load_dotenv()


class TestExtensive:
    def test_v3_network_leading(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        time.sleep(60)
        base_methods.authenticate_premium_user()
        decrypt_method = DecryptData()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v3/network/info/leading/extensive",
                                                headers=headers)
        response_data = response.json()
        decrypted_data = decrypt_method.decrypt_from_api(response_data.get("payload"), "extension")
        data = decrypted_data.get("result")
        assert response.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_v2_network_data(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        decrypt_method = DecryptData()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/network/data/extensive"
                                    f"?nodes_pool_id=3", headers=headers)
        response_data = response.json()
        decrypted_data = decrypt_method.decrypt_from_api(response_data.get("payload"), "extension")
        data = decrypted_data.get("result").get("data").get("ip_address")
        assert response.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_v2_network_info_leading(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        decrypt_method = DecryptData()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/network/info/leading/extensive"
                                    f"?nodes_pool_id=3", headers=headers)
        response_data = response.json()
        decrypted_data = decrypt_method.decrypt_from_api(response_data.get("payload"), "extension")
        data = decrypted_data.get("result").get("data")
        assert response.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_v2_network_info_leading(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        decrypt_method = DecryptData()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/network/info/leading/extensive",
                                    headers=headers)
        response_data = response.json()
        decrypted_data = decrypt_method.decrypt_from_api(response_data.get("payload"), "extension")
        data = decrypted_data.get("result").get("data")
        assert response.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)
