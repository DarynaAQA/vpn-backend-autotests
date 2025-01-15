import json
import os
import time

import pytest
import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn
from base_classes.test_utility import OutputConsoleResult
from methods_for_routes.base_methods import AvailabilityRoutes

load_dotenv()


class TestFeedback:
    def test_get_reasons_v2(self):
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
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-locale": "ua",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/120.0.0.0 Safari/537.36"
        }
        get_reasons = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/feedbacks/reasons",
                                    headers=headers)
        info_reasons = get_reasons.json()
        data = info_reasons.get("data")
        assert get_reasons.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_reasons_v3(self):
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
            "x-locale": "ua",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_reasons = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v3/feedbacks/reasons",
                                    headers=headers)
        info_reasons = get_reasons.json()
        data = info_reasons.get("data")
        assert get_reasons.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_like_feedback_v3(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute PUT request
            4. Compare status code of response
            5. Check info from response
        """
        for platform in DataIn.platform_feedback:
            headers = {
                "Authorization": f"Bearer {DataIn.token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-locale": "ua",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                    " like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            put_like = requests.put(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v3/feedbacks?type=1&"
                                    f"platform={platform}", headers=headers)
            like_response = put_like.json()
            data = like_response.get("success")
            assert put_like.status_code == 200
            assert data == True

    def test_dislike_feedback_v3(self):
        """
           STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute PUT request
            4. Compare status code of response
            5. Check info from response
        """
        for platform in DataIn.platform_feedback:
            headers = {
                "Authorization": f"Bearer {DataIn.token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-locale": "ua",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                    " like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            put_dislike = requests.put(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v3/feedbacks?type=2&"
                                        f"platform={platform}", headers=headers)
            dislike_response = put_dislike.json()
            data = dislike_response.get("success")
            assert put_dislike.status_code == 200
            assert data == True

    def test_like_feedback_v2(self):
        """
            STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute PUT request
            4. Compare status code of response
            5. Check info from response
        """
        for platform in DataIn.platform_feedback:
            headers = {
                "Authorization": f"Bearer {DataIn.token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-locale": "ua",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                    " like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            put_like = requests.put(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/feedbacks?type=1&"
                                    f"platform={platform}", headers=headers)
            like_response = put_like.json()
            data = like_response.get("success")
            assert put_like.status_code == 200
            assert data == True

    def test_dislike_feedback_v2(self):
        """
           STEPS:
            1. Execute user authorization
            2. Pass authorization token to Headers
            3. Execute PUT request
            4. Compare status code of response
            5. Check info from response
        """
        for platform in DataIn.platform_feedback:
            headers = {
                "Authorization": f"Bearer {DataIn.token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-locale": "ua",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                    " like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            put_dislike = requests.put(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/feedbacks?type=2&"
                                        f"platform={platform}", headers=headers)
            dislike_response = put_dislike.json()
            data = dislike_response.get("success")
            assert put_dislike.status_code == 200
            assert data == True

    def test_create_feedback_v2(self):
        """
           STEPS:
            1. Execute POST request
            2. Compare status code of response
            3. Check info from data
        """
        for platform in DataIn.platform_feedback:
            headers = {
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                    " like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            post_create_feedback = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/feedbacks",
                                                    headers=headers, data={
                "type": 2,
                "groups[]": 1,
                "reasons[]": 1,
                "source": "feedback",
                "country": "Ukraine",
                "detail": "TEST",
                "platform": f"{platform}",
                "locale": "ua"

            })
            create_feedback = post_create_feedback.json()
            feedback = create_feedback["data"]["id"]
            id_feedback = int(feedback)
            assert post_create_feedback.status_code == 201
            assert len([id_feedback]) > 0
            OutputConsoleResult.print_result([id_feedback])

    def test_create_feedback_uninstall_v2(self):
        """
           STEPS:
            1. Execute POST request
            2. Compare status code of response
            3. Check info from response
        """
        for platform in DataIn.platform_feedback:
            headers = {
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                    " like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            post_create_feedback = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/feedbacks",
                                                    headers=headers, data={
                "type": 2,
                "groups[]": 1,
                "reasons[]": 1,
                "source": "uninstall",
                "country": "Ukraine",
                "detail": "TEST",
                "platform": f"{platform}",
                "locale": "ua"

            })
            create_feedback_uninstall = post_create_feedback.json()
            feedback_uninstall = create_feedback_uninstall["data"]["id"]
            id_feedback = int(feedback_uninstall)
            assert post_create_feedback.status_code == 201
            assert len([id_feedback]) > 0
            OutputConsoleResult.print_result([id_feedback])

    def test_create_feedback_v3(self):
        """
           STEPS:
            1. Execute POST request
            2. Compare status code of response
            3. Check info from data
        """
        for platform in DataIn.platform_feedback:
            headers = {
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                    " like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            post_create_feedback = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v3/feedbacks",
                                                    headers=headers, data={
                "type": 2,
                "groups[]": 1,
                "reasons[]": 1,
                "source": "feedback",
                "country": "Ukraine",
                "detail": "TEST",
                "platform": f"{platform}",
                "locale": "ua",
                "domain": "xxx.xx2"
            })
            create_feedback = post_create_feedback.json()
            feedback = create_feedback["data"]["id"]
            id_feedback = int(feedback)
            assert post_create_feedback.status_code == 201
            assert len([id_feedback]) > 0
            OutputConsoleResult.print_result([id_feedback])

    def test_create_feedback_uninstall_v3(self):
        """
           STEPS:
            1. Execute POST request
            2. Compare status code of response
            3. Check info from response
        """
        for platform in DataIn.platform_feedback:
            headers = {
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                    " like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            post_create_feedback = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v3/feedbacks",
                                                    headers=headers, data={
                "type": 2,
                "groups[]": 1,
                "reasons[]": 1,
                "source": "uninstall",
                "country": "Ukraine",
                "detail": "TEST",
                "platform": f"{platform}",
                "locale": "ua",
                "domain": "xxx.xx2"
            })
            create_feedback_uninstall = post_create_feedback.json()
            feedback_uninstall = create_feedback_uninstall["data"]["id"]
            id_feedback = int(feedback_uninstall)
            assert post_create_feedback.status_code == 201
            assert len([id_feedback]) > 0
            OutputConsoleResult.print_result([id_feedback])

    @pytest.mark.parametrize("app", DataIn.uuid_apps)
    def test_like_feedback_v4(self, app):
        headers = {
            "UUID-APP": app.get("uuid"),
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-locale": "ua",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                " like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        data = {
            "type": 1,
            "reasons[]": 6,
            "source": "feedback",
            "country": "Ukraine",
            "locale": "ua",
            "detail": "TEST",
            "domain": "xxx.xx2",
        }
        response = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v4/feedbacks",
                                 headers=headers, data=json.dumps(data))
        response_data = response.json()
        data = response_data.get("data")
        assert response.status_code == 201
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    @pytest.mark.parametrize("app", DataIn.uuid_apps)
    def test_dislike_feedback_v4(self, app):
        headers = {
            "UUID-APP": app.get("uuid"),
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-locale": "ua",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                " like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        data = {
            "type": 2,
            "reasons": [10],
            "source": "feedback",
            "country": "Ukraine",
            "locale": "ua",
            "detail": "TEST",
            "domain": "xxx.xx2",
        }
        response = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v4/feedbacks",
                                 headers=headers, data=json.dumps(data))
        response_data = response.json()
        print(response_data)
        data = response_data.get("data")
        assert response.status_code == 201
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    @pytest.mark.parametrize("app", DataIn.uuid_apps)
    def test_feedback_uninstall_v4(self, app):
        headers = {
            "UUID-APP": app.get("uuid"),
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-locale": "ua",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                                " like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        data = {
            "type": 1,
            "reasons[]": 5,
            "source": "uninstall",
            "country": "Ukraine",
            "locale": "ua",
            "detail": "TEST",
            "domain": "xxx.xx2",
        }
        response = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v4/feedbacks",
                                 headers=headers, data=json.dumps(data))
        response_data = response.json()
        data = response_data.get("data")
        assert response.status_code == 201
        assert len(data) > 0
        OutputConsoleResult.print_result(data)
