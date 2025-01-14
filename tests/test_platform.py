import os

import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn
from base_classes.test_utility import OutputConsoleResult
from methods_for_routes.base_methods import AvailabilityRoutes

load_dotenv()


class TestPlatform:
    def test_payment_failed(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        DataIn.token = base_methods.authenticate_free_user()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        post_payment_failed = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/platform/android/"
                                            f"payment/failed", headers=headers)
        payment_failed = post_payment_failed.json()
        data = payment_failed.get("status")
        assert post_payment_failed.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_adblock_rules(self):
        """
            STEPS:
            1. Execute GET request
            2. Compare status code of response
            3. Сheck that the key "rules" are not empty
        """
        get_adblock_rules = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/platform/adblock/rules")
        adblock_rules = get_adblock_rules.json()
        data = adblock_rules.get("rules")
        assert get_adblock_rules.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_ip(self):
        """
            STEPS
            1. Execute GET request
            2. Compare status code of response
            3. Сheck that the key "ip" are not empty
        """
        get_ip = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/ip")
        ip = get_ip.json()
        data = ip.get("ip")
        assert get_ip.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_platform_link(self):
        base_methods = AvailabilityRoutes()
        DataIn.token = base_methods.authenticate_premium_user()
        headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_platform_link = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/platform/link",
                                            headers=headers)
        assert get_platform_link.status_code == 200
