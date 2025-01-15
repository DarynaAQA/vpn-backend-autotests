class DataIn:

    token = ""

    platform_param = [
        "app/ios/version?store=ios",
        "app/windows/version?store=microsoft",
        "app/macos/version?store=apple",
        "app/android/version?store=play_market",
        "app/android/version?store=amazon",
        "app/android/version?store=huawei",
    ]

    store_list = ["huawei", "play_market", "amazon", "microsoft", "macos"]

    platform_feedback = [
        "yandex",
        "windows",
        "android",
        "macos",
        "ios",
        "chrome",
        "firefox",
        "opera",
        "edge",
    ]

    platforms = [
        "windows",
        "android",
        "macos",
        "ios",
    ]
    
    uuid_apps = [
        {
            "uuid": "a2f712aa-c30a-4811-82b3-af6a527118f5",
            "platform": "iOS (default)",
        },

        {
            "uuid": "5ccc3764-395a-4b3c-a009-463e71a910a0",
            "platform": "Windows (default)",
        },
        {
            "uuid": "883f808d-771c-4da3-b798-915fcbe2da7d",
            "platform": "iOS (default)",
        }
    ]
