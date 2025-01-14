import os
import time

import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn
from base_classes.test_utility import OutputConsoleResult
from methods_for_routes.base_methods import AvailabilityRoutes

load_dotenv()


class TestUser:
    def test_create_smart_filter(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        time.sleep(60)
        DataIn.token = base_methods.authenticate_premium_user()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache"
        }

        payload = {
            "type": "smart-filter",
            "settings": [
                "https://domain.com"
            ]
        }
        create_smart_filter = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/settings",
                                            headers=headers, data=payload)
        info_smart_filter = create_smart_filter.json()
        assert create_smart_filter.status_code == 200
        assert info_smart_filter["data"]["settings"] == "https://domain.com"

    def test_get_smart_filter(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_smart_filter = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/settings?"
                                        f"type=smart-filter", headers=headers)
        info_smart_filter = get_smart_filter.json()
        assert get_smart_filter.status_code == 200
        assert info_smart_filter["data"]["type"] == "smart-filter"

    def test_create_adblock(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache"
        }

        payload = {
                "type": "adblock",
                "settings": [
                    "https://domain.com"
                ]
        }
        create_adblock = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/settings",
                                        headers=headers, data=payload)
        info_adblock = create_adblock.json()
        assert create_adblock.status_code == 200
        assert info_adblock["data"]["settings"] == "https://domain.com"

    def test_get_adblock(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_adblock = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/settings?type=adblock",
                                    headers=headers)
        info_adblock = get_adblock.json()
        assert get_adblock.status_code == 200
        assert info_adblock["data"]["type"] == "adblock"

    def test_add_support_ticket(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache"
        }
        add_support_ticket = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/support/ticket",
                                            headers=headers, data={
            "name": "test",
            "email": "test@test.com",
            "description": "test"
        })
        support_ticket = add_support_ticket.json()
        assert add_support_ticket.status_code == 200
        assert support_ticket["data"]["success"] == True

    def test_add_support_ticket_v2(self):
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache"
        }
        add_support_ticket = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/user/support/"
                                            f"ticket", headers=headers, data={
            "name": "Name",
            "email": "test@test.com",
            "description": "Description text",
            "subject": "Test"
        })
        support_ticket = add_support_ticket.json()
        assert add_support_ticket.status_code == 200
        assert support_ticket["data"]["success"] == True

    def test_get_user_info(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36"
        }
        get_user_info = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/", headers=headers)
        user_info = get_user_info.json()
        data = user_info.get("data").get("email")
        assert get_user_info.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_v2_user_info(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_user_info = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/user/", headers=headers)
        user_info = get_user_info.json()
        data = user_info.get("data").get("email")
        assert get_user_info.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_v3_user_info(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_user_info = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v3/user/", headers=headers)
        user_info = get_user_info.json()
        data = user_info.get("data").get("email")
        assert get_user_info.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_add_nodes_pool_to_favorite(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache"
        }
        payload = {
            "nodes_pool_id": 5
        }
        post_nodes_pools_favorites = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/"
                                                    f"nodes-pools/favorites", headers=headers, data=payload)
        assert post_nodes_pools_favorites.status_code == 200

    def test_get_user_favorite_nodes_pools_list(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache"
        }
        get_nodes_pools_favorites = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/"
                                                    f"nodes-pools/favorites", headers=headers)
        nodes_pools_favorites = get_nodes_pools_favorites.json()
        data = nodes_pools_favorites.get("data")
        assert get_nodes_pools_favorites.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_remove_nodes_pool_from_favorite(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache"
        }
        post_remove_nodes_pools_favorites = requests.delete(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/"
                                                    f"user/nodes-pools/favorites?nodes_pool_id=5", headers=headers)

        assert post_remove_nodes_pools_favorites.status_code == 200

    def test_change_user_password(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache"
        }
        post_change_user_password = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/password/"
                                                    f"change", headers=headers, data={
            "password": os.getenv("NEW_PASSWORD_FOR_PREMIUM_USER"),
            "old_password": os.getenv("OLD_PASSWORD_FOR_PREMIUM_USER")
        })
        change_user_password = post_change_user_password.json()
        data = change_user_password.get("data").get("token")
        assert post_change_user_password.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)
        base_methods.change_password_back_premium_user()

    def test_reset_user_password(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        DataIn.token = base_methods.authenticate_premium_user()
        load_dotenv()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        post_reset_user_password = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/password/"
                                                    f"reset", headers=headers, data={
                "password": os.getenv("OLD_PASSWORD_FOR_PREMIUM_USER")
        })
        reset_user_password = post_reset_user_password.json()
        data = reset_user_password.get("data").get("token")
        assert post_reset_user_password.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_confirm_user_email(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute GET request
            4. Compare status code of response
            5. Check info from data
        """
        base_methods = AvailabilityRoutes()
        DataIn.token = base_methods.authenticate_premium_user()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache"
        }
        post_confirm_user_email = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/confirm",
                                                headers=headers)
        confirm_user_email = post_confirm_user_email.json()
        data = confirm_user_email.get("data").get("token")
        assert post_confirm_user_email.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_request_email_confirmation_letter(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
        """
        base_methods = AvailabilityRoutes()
        DataIn.token = base_methods.authenticate_premium_user()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36"

        }
        post_user_confirm = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/confirm/send",
                                            headers=headers)
        assert post_user_confirm.status_code == 200
