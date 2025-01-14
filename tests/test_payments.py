import os
import time

import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn
from base_classes.test_utility import OutputConsoleResult
from methods_for_routes.base_methods import AvailabilityRoutes

load_dotenv()


class TestPayments:

    def test_get_offers_list(self):
        base_methods = AvailabilityRoutes()
        time.sleep(60)
        DataIn.token = base_methods.authenticate_premium_user()
        headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
            "X-Platform-Key": "ios",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_offers_list = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/offers", headers=headers)
        offers_list = get_offers_list.json()
        data = offers_list.get("data")
        assert get_offers_list.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_customer_portal_session(self):
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "Content-type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36"
        }
        get_customer_portal_session = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/"
            f"subscriptions/stripe/customer-portal-session?return_url=http://example.com/account", headers=headers)
        customer_portal_session = get_customer_portal_session.json()
        data = customer_portal_session.get("success")
        assert get_customer_portal_session.status_code == 200
        assert data == False
