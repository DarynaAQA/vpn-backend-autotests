import os

import requests
from dotenv import load_dotenv

from base_classes.data_in import DataIn
from base_classes.test_utility import OutputConsoleResult

load_dotenv()


class TestApplication:
    def test_get_latest_app_version(self):
        """
            Gets the latest version of apps depending on the store.
        """
        for param in DataIn.platform_param:
            get_version_app = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/{param}")
            version_app = get_version_app.json()
            data = version_app.get("data").get("version")
            assert get_version_app.status_code == 200
            assert len(data) > 0
            OutputConsoleResult.print_result(data)

    def test_get_config(self):
        """
            Returns the config for connecting to VPN.
        """
        for store in DataIn.store_list:
            get_link_feedback = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/app/config?store="
                                                f"{store}")
            link_feedback = get_link_feedback.json()
            data = link_feedback.get("data").get("trustpilot_url")
            assert get_link_feedback.status_code == 200
            assert len(data) > 0
            OutputConsoleResult.print_result(data)
