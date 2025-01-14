import json
import os
import time

import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn
from base_classes.test_utility import OutputConsoleResult
from methods_for_routes.base_methods import AvailabilityRoutes
from methods_for_routes.decrypt_payload import DecryptData

load_dotenv()


class TestNodesPools:
    def test_get_nodes_pools(self):
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
        DataIn.token = base_methods.authenticate_premium_user()
        decrypt_method = DecryptData()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_nodes_pools = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v1/network/info/leading",
                                        headers=headers)
        nodes_pools = get_nodes_pools.text
        decrypted_message = decrypt_method.main(nodes_pools)
        json_decrypted_message = json.loads(decrypted_message)
        data = json_decrypted_message.get("data")
        assert get_nodes_pools.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_nodes_pools_user(self):
        decrypt_method = DecryptData()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_nodes_pools = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v1/network/user/leading",
                                        headers=headers)
        nodes_pools = get_nodes_pools.text
        decrypted_message = decrypt_method.main(nodes_pools)
        json_decrypted_message = json.loads(decrypted_message)
        data = json_decrypted_message.get("data")
        assert get_nodes_pools.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_add_nodes_pools_user(self):
        base_methods = AvailabilityRoutes()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_nodes_pools = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v1/network/user/leading",
                                        headers=headers, data={"nodes_pool_id": 4})
        nodes_pools = get_nodes_pools.json()
        payload = nodes_pools["payload"]
        decrypted_message = base_methods.decrypt_payload(payload=payload, service="default")
        assert get_nodes_pools.status_code == 200
        assert decrypted_message["success"] == True

    def test_delete_nodes_pools_user(self):
        base_methods = AvailabilityRoutes()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_nodes_pools = requests.delete(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v1/network/user/"
                                            f"leading?nodes_pool_id=4", headers=headers)
        nodes_pools = get_nodes_pools.json()
        payload = nodes_pools["payload"]
        decrypted_message = base_methods.decrypt_payload(payload=payload, service="default")
        assert get_nodes_pools.status_code == 200
        assert decrypted_message["success"] == True

    def test_get_nodes_pools_other_route(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_nodes_pools = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/nodes-pools",
                                        headers=headers)
        nodes_pools = get_nodes_pools.json()
        data = nodes_pools.get("data")
        assert get_nodes_pools.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_nodes_pools_lite(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_nodes_pools_lite = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/nodes-pools-lite?"
                                            f"country=us", headers=headers)
        nodes_pools_lite = get_nodes_pools_lite.json()
        data = nodes_pools_lite.get("data")
        assert get_nodes_pools_lite.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_pools_load(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_pools_load = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/pools-load",
                                        headers=headers)
        pools_load = get_pools_load.json()
        data = pools_load.get("data")
        assert get_pools_load.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_dev_nodes_pools_lite(self):
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_nodes_pools_lite = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/lite/dev/v1/nodes-pools",
                                            headers=headers)
        nodes_pools_lite = get_nodes_pools_lite.json()
        data = nodes_pools_lite.get("data")
        assert get_nodes_pools_lite.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_v2_nodes_pools(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_nodes_pools = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/nodes-pools",
                                            headers=headers)
        nodes_pools = get_nodes_pools.json()
        data = nodes_pools.get("data")
        assert get_nodes_pools.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_v2_pools_load(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_pools_load = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/pools-load",
                                        headers=headers)
        pools_load = get_pools_load.json()
        data = pools_load.get("data")
        assert get_pools_load.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_network_info_leading_extensive_additional(self):
        base_methods = AvailabilityRoutes()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
        }
        get_network_info_leading_extensive = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/"
                                                          f"network/info/leading/extensive/additional", headers=headers)

        network_info_leading_extensive_json = get_network_info_leading_extensive.json()
        payload = network_info_leading_extensive_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="extension", payload=payload)
        assert get_network_info_leading_extensive.status_code == 200
        assert len(decrypted_date) > 0
        OutputConsoleResult.print_result(decrypted_date)

    def test_network_info_leading_extensive_primary(self):
        base_methods = AvailabilityRoutes()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
        }
        get_network_info_leading_extensive = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/"
                                                          f"network/info/leading/extensive/primary", headers=headers)

        network_info_leading_extensive_json = get_network_info_leading_extensive.json()
        payload = network_info_leading_extensive_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="extension", payload=payload)
        assert get_network_info_leading_extensive.status_code == 200
        assert len(decrypted_date) > 0
        OutputConsoleResult.print_result(decrypted_date)

    def test_network_info_leading_primary(self):
        base_methods = AvailabilityRoutes()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
        }
        get_network_info_leading = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/"
                                                f"network/info/leading/primary", headers=headers)
        network_info_leading_json = get_network_info_leading.json()
        payload = network_info_leading_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="default", payload=payload)
        assert get_network_info_leading.status_code == 200
        assert len(decrypted_date) > 0
        OutputConsoleResult.print_result(decrypted_date)

    def test_network_info_leading_additional(self):
        base_methods = AvailabilityRoutes()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
        }
        get_network_info_leading = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/network/info/"
                                                f"leading/additional", headers=headers)
        network_info_leading_json = get_network_info_leading.json()
        payload = network_info_leading_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="default", payload=payload)
        assert get_network_info_leading.status_code == 200
        assert len(decrypted_date) > 0
        OutputConsoleResult.print_result(decrypted_date)

    def test_network_user_leading_extensive_v2_post(self):
        base_methods = AvailabilityRoutes()
        DataIn.token = base_methods.authenticate_premium_user()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",

        }
        post_network_user_leading_extensive = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/"
                                                            f"network/user/leading/extensive", headers=headers, data={
            "nodes_pool_id": 6
        })
        network_user_leading_extensive_json = post_network_user_leading_extensive.json()
        payload = network_user_leading_extensive_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="extension", payload=payload)
        assert post_network_user_leading_extensive.status_code == 200
        assert len(decrypted_date) > 0
        OutputConsoleResult.print_result(decrypted_date)

    def test_network_user_leading_extensive_v2_delete(self):
        base_methods = AvailabilityRoutes()
        DataIn.token = base_methods.authenticate_premium_user()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",

        }
        post_network_user_leading_extensive = requests.delete(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/"
                                                              f"network/user/leading/extensive?nodes_pool_id=6",
                                                              headers=headers)
        network_user_leading_extensive_json = post_network_user_leading_extensive.json()
        payload = network_user_leading_extensive_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="extension", payload=payload)
        assert post_network_user_leading_extensive.status_code == 200
        assert len(decrypted_date) > 0
        OutputConsoleResult.print_result(decrypted_date)