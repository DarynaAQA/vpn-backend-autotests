import datetime
import os

import jwt
import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn
from base_classes.test_utility import OutputConsoleResult
from methods_for_routes.base_methods import AvailabilityRoutes

load_dotenv()


class TestAuth:

    def test_register_new_user(self):
        """
            STEPS:
            1. Send a POST request with the user's email
            2. Compare status code of response
            3. Сheck for the presence of an authorization token in the response
        """
        date_registration = datetime.datetime.now().strftime("%d%m%Y%H%M")
        registration = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/register", data={
            "email": f"darina.test{date_registration}@gmail.com"
        })
        check_register = registration.json()
        data = check_register.get("data").get("token")
        assert registration.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_invalidate_token(self):
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
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        post_invalidate_token = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/token/invalidate",
                                                headers=headers)
        invalidate_token = post_invalidate_token.json()
        data = invalidate_token.get("data").get("success")
        assert post_invalidate_token.status_code == 200
        assert data == True

    def test_authenticate_premium_user(self):
        """
            STEPS:
            1. Send a POST request with the Premium user's email and password
            2. Compare status code of response
            3. Сheck for the presence of an authorization token in the response
        """
        authorization_user = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/login", data={
            "email": os.getenv("PREMIUM_EMAIL"),
            "password": os.getenv("PREMIUM_PASSWORD")
        })
        authorization = authorization_user.json()
        data = authorization.get("data").get("token")
        assert authorization_user.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_authenticate_free_user(self):
        """
            STEPS:
            1. Send a POST request with the Free user's email and password
            2. Compare status code of response
            3. Сheck for the presence of an authorization token in the response
        """
        authorization_user = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/login", data={
            "email": os.getenv("FREE_EMAIL"),
            "password": os.getenv("FREE_PASSWORD")
        })
        authorization = authorization_user.json()
        data = authorization.get("data").get("token")
        assert authorization_user.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_check_authentication_token(self):
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
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36"
        }
        check_token = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/token/check", headers=headers)
        authentication_token = check_token.json()
        data = authentication_token.get("data").get("is_valid")
        assert check_token.status_code == 200
        assert data == True

    def test_refresh_authentication_token(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
            5. Сheck for the presence of an authorization token in the response
        """
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36"
        }
        get_token_refresh = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/token/refresh",
                                            headers=headers)
        token_refresh = get_token_refresh.json()
        data = token_refresh.get("data").get("token")
        assert get_token_refresh.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_logout_user(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute POST request
            4. Compare status code of response
        """
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36"
        }
        logout_user = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/logout", headers=headers)
        assert logout_user.status_code == 200

    def test_restore_access_to_account(self):
        """
            STEPS:
            1. Send a POST request with the user's email
        """
        restore_account = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/forgot", data={
                "email": os.getenv("EMAIL")
        })
        assert restore_account.status_code == 200

    def test_delete_user(self):
        """
        Test the deletion of a user.

        This test performs the following steps:
        1. Authenticates a premium user.
        2. Registers a new user with a unique email.
        3. Extracts the token and decodes it to get the user ID.
        4. Deletes the user using the extracted user ID.
        5. Asserts that the deletion was successful and the status code is 200.

        Raises:
            AssertionError: If the deletion was not successful or the status code is not 200.
        """
        base_methods = AvailabilityRoutes()
        base_methods.authenticate_premium_user()
        headers = {
            "x-platform-key": "test",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36"
        }
        date_registration = datetime.datetime.now().strftime("%d%m%Y%H%M")
        registration = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/register", data={
            "email": f"darina.test{date_registration}@gmail.com"}, headers=headers)
        check_register = registration.json()
        token = check_register.get("data").get("token")
        decoded_payload = jwt.decode(token, options={"verify_signature": False})
        id = decoded_payload.get("sub")
        headers.setdefault("Authorization", f"Bearer {DataIn.token}")
        delete_user = requests.delete(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/test/user/{id}",
                                      headers=headers)
        delete_user_data = delete_user.json()
        data = delete_user_data.get("success")
        assert delete_user.status_code == 200
        assert data == True
