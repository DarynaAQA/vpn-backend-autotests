import os

import requests
from dotenv import load_dotenv

from base_classes.test_utility import OutputConsoleResult

load_dotenv()


class TestAds:

    def test_ads(self):
        get_ads = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/ads")
        ads = get_ads.json()
        data = ads.get("data")
        assert get_ads.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_ads_desktop(self):
        get_ads_desktop = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/ads-desktop")
        ads_desktop = get_ads_desktop.json()
        data = ads_desktop.get("data")
        assert get_ads_desktop.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_ads_desktop_interstitial(self):
        get_ads_interstitial = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/ads-interstitial")
        ads_interstitial = get_ads_interstitial.json()
        data = ads_interstitial.get("data")
        assert get_ads_interstitial.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_ads_interstitial_vpnly(self):
        get_ads_interstitial_vpnly = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}"
                                                    f"/ads-interstitial-vpnly")
        ads_interstitial_vpnly = get_ads_interstitial_vpnly.json()
        data = ads_interstitial_vpnly.get("data")
        assert get_ads_interstitial_vpnly.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_ads_v2(self):
        get_ads = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/ads")
        ads = get_ads.json()
        data = ads.get("data")
        assert get_ads.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_ads_test_v2(self):
        get_ads = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/ads-test")
        ads = get_ads.json()
        data = ads.get("data")
        assert get_ads.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_ads_vpnly_v2(self):
        get_ads = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/v2/ads-vpnly")
        ads = get_ads.json()
        data = ads.get("data")
        assert get_ads.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)

    def test_get_ads_desktop_test(self):
        headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36"
        }
        get_ads_desktop_test = requests.get(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/test/ads-desktop",
                                            headers=headers)
        ads_desktop_test = get_ads_desktop_test.json()
        data = ads_desktop_test.get("data")
        assert get_ads_desktop_test.status_code == 200
        assert len(data) > 0
        OutputConsoleResult.print_result(data)
