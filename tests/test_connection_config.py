import json
import os

import pytest
import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn
from base_classes.test_utility import OutputConsoleResult
from methods_for_routes.base_methods import AvailabilityRoutes
from methods_for_routes.decrypt_payload import DecryptData

load_dotenv()


class TestConnectionConfig:
    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        self.base_methods = AvailabilityRoutes()
        self.base_methods.authenticate_premium_user()
    
    def test_windows_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/network/data"
                                                f"/warmed?nodes_pool_id=56", headers=headers)
        connection_config = get_connection_config.text
        decrypted_message = decrypt_method.main(connection_config)
        json_decrypted_message = json.loads(decrypted_message)
        data = json_decrypted_message["data"]
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_macos_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/network/data/"
                                                f"multiplied?nodes_pool_id=56", headers=headers)
        connection_config = get_connection_config.text
        decrypted_message = decrypt_method.main(connection_config)
        json_decrypted_message = json.loads(decrypted_message)
        data = json_decrypted_message["data"]
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_ios_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/network/data/"
                                                f"improved?nodes_pool_id=56", headers=headers)
        connection_config = get_connection_config.text
        decrypted_message = decrypt_method.main(connection_config)
        json_decrypted_message = json.loads(decrypted_message)
        data = json_decrypted_message["data"]
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_android_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/network/data/"
                                                f"adapted?nodes_pool_id=56", headers=headers)
        connection_config = get_connection_config.text
        decrypted_message = decrypt_method.main(connection_config)
        json_decrypted_message = json.loads(decrypted_message)
        data = json_decrypted_message["data"]
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_encrypted_route_windows_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/g67sml6l/w89mna2s"
                                                f"?nodes_pool_id=3", headers=headers)
        connection_config = get_connection_config.json()
        decrypted_data = decrypt_method.decrypt_from_api(connection_config.get("payload"), "windows_api_v3")
        data = decrypted_data.get("result")
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_encrypted_route_ios_blue_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/k22lG50g/ib6we9lt"
                                                f"?nodes_pool_id=3", headers=headers)
        connection_config = get_connection_config.json()
        decrypted_data = decrypt_method.decrypt_from_api(connection_config.get("payload"), "ios_blue_api_v3")
        data = decrypted_data.get("result")
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_encrypted_route_android_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/kE7icfC5/aGh1km71"
                                                f"?nodes_pool_id=3", headers=headers)
        connection_config = get_connection_config.json()
        decrypted_data = decrypt_method.decrypt_from_api(connection_config.get("payload"), "android_api_v3")
        data = decrypted_data.get("result")
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_encrypted_route_ios_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/qMAHrQiM/i46weq0t"
                                                f"?nodes_pool_id=3", headers=headers)
        connection_config = get_connection_config.json()
        decrypted_data = decrypt_method.decrypt_from_api(connection_config.get("payload"), "ios_api_v3")
        data = decrypted_data.get("result")
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_encrypted_route_ios_dark_blue_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/uDXkUEuA/idb1e80p"
                                                f"?nodes_pool_id=3", headers=headers)
        connection_config = get_connection_config.json()
        decrypted_data = decrypt_method.decrypt_from_api(connection_config.get("payload"), "ios_dark_blue_api_v3")
        data = decrypted_data.get("result")
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_encrypted_route_macos_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/uiJNI8uv/mJ8kwe0q"
                                                f"?nodes_pool_id=3", headers=headers)
        connection_config = get_connection_config.json()
        decrypted_data = decrypt_method.decrypt_from_api(connection_config.get("payload"), "macos_api_v3")
        data = decrypted_data.get("result")
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_lite_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/lite/v1/connection/config"
                                                f"?nodes_pool_id=126", headers=headers)
        connection_config = get_connection_config.json()
        decrypted_data = decrypt_method.decrypt_from_api(connection_config.get("payload"), "v1_lite")
        data = decrypted_data.get("result")
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_v1_connection_config(self):
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
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v1/network/connection/"
                                             f"config?nodes_pool_id=126", headers=headers)
        connection_config = get_connection_config.json()
        decrypted_data = decrypt_method.decrypt_from_api(connection_config.get("payload"), "v1_lite")
        data = decrypted_data.get("result")
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)
    
    def test_connection_config_windows(self):
        base_methods = AvailabilityRoutes()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "UUID-APP": "b37ded9b-ae66-40a4-a8e6-e6c833c92284",
            "FVP-APP": "eyJpdiI6InorRHhDamRRRDdOVHQraXR6elBDdkE9PSIsInZhbHVlIjoiR1VIT2NQb2hYdXFWVFk4bjZ0dThuMHRzUm9FTC"
                       "txTXNoYW50WVY3RGtxTkgzdzI0dnJFV2lIZUk0S0xyMXJRdDlBd3ltNG1TQkdnSHJPTCtRcnNqZ3lNTUk3RVhDQjZucncvV"
                       "EJFYUhFUnNXMWxpM0NkclUwQVlOc0o5N2FxWm4iLCJtYWMiOiI5YmM1YmM4M2RjZTVlMGU4ZDlhODk1ZjEyNjMyMmU2MDR"
                       "hMDVlYzA1MjhhZWYxM2M2YjMxZjE3MmE4OGU5NDBmIiwidGFnIjoiIn0="
        }
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/0r7Fj0KlE46nBBYGla57/"
                                             f"wQuDj7U8IJa?nodes_pool_id=3", headers=headers)
        connection_config_json = get_connection_config.json()
        payload = connection_config_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="windows_api_v3", payload=payload)
        data = decrypted_date["result"]
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_connection_config_macos(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "UUID-APP": "11b2e2b7-7320-4bbf-a339-c27d0fdaaf4a",
            "FVP-APP": "eyJpdiI6Ik5iMTh6aXJ2TFdDUXpEdzFWS09PeUE9PSIsInZhbHVlIjoidGdZcUQwSkI2THpteTFBT0hERE51YklNWlBqbj"
                       "RUeE0yUjRUYmpxN0h6TFZ3WFZMa2ozR2RQeDk2TUMzR3p4NDdTalJJZTZ0Qjg1L29UTVFaWU5BR0ZrWjZybVlteW51bFVx"
                       "MXIzU2pGRTI4NnYwWmxuaTJOL2J5cWdhN1R5TisiLCJtYWMiOiI0ZTgzMWFmMzIzZGI3NThlMTJlYjUzMjBiNzZmOWIxZm"
                       "UzY2RmZThiMjU3MmExMzA3NDNjOTFlYTBjYTY3MWU1IiwidGFnIjoiIn0="
        }
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/JISl8NAlUKmVQLeD3EJE/"
                                             f"mA4G8BF154m?nodes_pool_id=3", headers=headers)
        connection_config_json = get_connection_config.json()
        payload = connection_config_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="macos_api_v3", payload=payload)
        data = decrypted_date["result"]
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_connection_config_ios(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "UUID-APP": "a2f712aa-c30a-4811-82b3-af6a527118f5",
            "FVP-APP": "eyJpdiI6Ii9oNUpsRTZ5WWNNMnNYYmNvUVlCd0E9PSIsInZhbHVlIjoicW9lRGZETXRHNlBhQnhVSmRHZlh4Z1ptL2tMR0"
                       "c1bjg1WmxVWWJaVWprajZpakZlcEEySTFRZ3d0RXJxek9uUnhXRytSMWJ4SFNwNFVkeG5LZlFQUXZwWmIzcStaY2Z2SUY4Q"
                       "1BTRDBKNC94cW9XTWdYUzREQzNoWTFEWlZPSjMiLCJtYWMiOiIzNTQwMzRjZDk0YjYwNTRkZWMyZDJiYTQ4N2UwYzQyNGMy"
                       "ODNiNzIzZGNkODg3YTc3ZDNjZjNjMGY0NTkyYWEyIiwidGFnIjoiIn0="
        }
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/YfYF8rW38OZ3jfgMN7BB/"
                                             f"iDfe7gpYafS?nodes_pool_id=3", headers=headers)
        connection_config_json = get_connection_config.json()
        payload = connection_config_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="ios_api_v3", payload=payload)
        data = decrypted_date["result"]
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_connection_config_ios_dark_blue(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "UUID-APP": "b1cac0dd-4918-461b-8594-3c8185aaeff7",
            "FVP-APP": "eyJpdiI6IlpmSnNQUDd1Tno4Tk0yeTNkUjRpS2c9PSIsInZhbHVlIjoiZmNWZlJFWC9Fc0Vsd1VvYmExaSs5ZTFXZ0lMMT"
                       "E0a0F3VXN5eEI0ditYQlI1QlNiRmhTSlErL1NHRnUxaW1Wb2Y0KzYxeE9QQXUrd2RhNTJzUWtGMmVGUUNSMG1NMWV5ZWZv"
                       "ZFBaWS9LamFmZnBjTDZrZFZla1BHeUNnUm92T2UiLCJtYWMiOiI0ZDhiNzc1MWU0YTU0ZTZhYTE1MWVkMDUzZjllYWUyNG"
                       "NhYzZhMTZjZTk0YjBkN2U0MWRkMTU3ZDBhMTk2ODQ5IiwidGFnIjoiIn0="
        }
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/a9ZYujQ0Il1Mm8qy1kEi/"
                                             f"idbYBd7u1no?nodes_pool_id=3", headers=headers)
        connection_config_json = get_connection_config.json()
        payload = connection_config_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="ios_dark_blue_api_v3", payload=payload)
        data = decrypted_date["result"]
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_connection_config_ios_blue(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "UUID-APP": "8f07a0ce-f877-4b85-8d9e-623e162d44a4",
            "FVP-APP": "eyJpdiI6ImN1ZGJyOHUveFRneGt6R1hRY2szYlE9PSIsInZhbHVlIjoiN2llbS9XWTJzZG0zeFgrNmFOelpqUmg5aHBuNHR"
                       "vR0s1Rnh1THN0WGRaeEl3TlByLzVPZ3NZaUMrRnFlUUlMK3BvMkNMT1c1Q0I4VVBLVFNSWUUweHdzcGZkVTlPRkgyR0VOUk"
                       "lYRjBJQXo4NE03VGtva2JaMG0vdkdqRzYrN20iLCJtYWMiOiIwYmQ1YzE1MzBhMDQ2ZGYxMWVlMGU4ODRlNWU3NTQxNWJiN"
                       "WNhMzYzZjFlYmIwMGQxZDViZmYwMjY4YWQ4MjI1IiwidGFnIjoiIn0="
        }
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/es1bxyZOr4yJ9U2QbhKu/"
                                             f"idUJ4wa748?nodes_pool_id=3", headers=headers)
        connection_config_json = get_connection_config.json()
        payload = connection_config_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="ios_blue_api_v3", payload=payload)
        data = decrypted_date["result"]
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_connection_ssl_check(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        get_connection_ssl_check = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/connection/ssl/check",
                                                headers=headers)
        connection_ssl_check_json = get_connection_ssl_check.json()
        assert get_connection_ssl_check.status_code == 200
        assert len(connection_ssl_check_json) > 0
        OutputConsoleResult.print_result(connection_ssl_check_json)

    def test_connection_config_android(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "UUID-APP": "653d0472-29bc-4591-944b-068f980ebbaf",
            "FVP-APP": "eyJpdiI6InVSTURnSW1IUnl0djZuUWFBVCtMRlE9PSIsInZhbHVlIjoiRFdVTFlnaVNkdHVRUHdNNHB4U2lvT0xWWCt4WDU"
                       "waTFjL0hIakdWMmdTNTFCSFB0WnpyLys5d3p0eDVFNjFBRityZ3RKUVBaSWpXN0lDRUFHd09HT211YTBaZ1FQVzhiUnVaM"
                       "zBBUGNHeVBQVXgxdHZqVjg4SzdRYjlHTXR5QkQiLCJtYWMiOiJhZTAwMGIyMTVkYTQ0NGJlOThjOWJjODI0MzcyNTY0MTY"
                       "1NWI0MjE3NTZjMzU4MjE5YWQwOTE0M2FjYzc0YmQwIiwidGFnIjoiIn0="
        }
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/fZZSpt5FFJSsBhv9FwR0/"
                                             f"aE8S487E9cJ?nodes_pool_id=3", headers=headers)
        connection_config_json = get_connection_config.json()
        payload = connection_config_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="android_api_v3", payload=payload)
        data = decrypted_date["result"]
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    @pytest.mark.parametrize("platform", DataIn.platforms)
    def test_optimized_connection_config(self, platform):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        get_connection_config = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v1/optimized/"
                                             f"connection/config?nodes_pool_id=3&platform={platform}", headers=headers)
        connection_config_json = get_connection_config.json()
        payload = connection_config_json["payload"]
        decrypted_date = base_methods.decrypt_payload(service="default", payload=payload)
        data = decrypted_date.get("result")
        assert get_connection_config.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)
