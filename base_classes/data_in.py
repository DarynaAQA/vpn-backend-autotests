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
            "platform": "Planet iOS (default)",
        },
        {
            "uuid": "653d0472-29bc-4591-944b-068f980ebbaf",
            "platform": "Planet Android (default)",
        },
        {
            "uuid": "11b2e2b7-7320-4bbf-a339-c27d0fdaaf4a",
            "platform": "Planet MacOS (default)",
        },
        {
            "uuid": "b37ded9b-ae66-40a4-a8e6-e6c833c92284",
            "platform": "Planet Windows (default)",
        },
        {
            "uuid": "3b543428-58c0-4d33-876f-a3535895f990",
            "platform": "Planet Linux (default)",
        },
        {
            "uuid": "417d6c71-0a98-4215-8c97-bba837b15161",
            "platform": "Planet Chrome (default)",
        },
        {
            "uuid": "d87bbbce-f851-4033-be60-67ad41a074fc",
            "platform": "Planet Firefox (default)",
        },
        {
            "uuid": "507fa4d4-0270-4698-a677-8baa8f9ca989",
            "platform": "Planet Opera (default)",
        },
        {
            "uuid": "722b02d2-a7e6-42d9-bb1d-4b06a3b0b546",
            "platform": "Planet Edge (default)",
        },
        {
            "uuid": "15f9d3fa-727e-4d8c-a7ab-0442292792b4",
            "platform": "Planet Yandex (default)",
        },
        {
            "uuid": "3ae1cd40-f915-469b-ac4f-6d598743d200",
            "platform": "Planet Site (default)",
        },
        {"uuid": "8f07a0ce-f877-4b85-8d9e-623e162d44a4", "platform": "Planet iOS Blue"},
        {
            "uuid": "ed2037e5-8859-4f29-bb29-7ef2d28332f1",
            "platform": "Planet Android Blue",
        },
        {
            "uuid": "b1cac0dd-4918-461b-8594-3c8185aaeff7",
            "platform": "Planet iOS Dark Blue",
        },
        {
            "uuid": "77583666-eaa2-4f15-b5d0-d3e03bcf5f0c",
            "platform": "Planet Android Dark Blue",
        },
        {"uuid": "54ae0088-b760-4cbf-8baa-e8ad1d30d091", "platform": "Lite CA Android"},
        {"uuid": "89919402-88cd-480f-9c6d-c382a2053a0c", "platform": "Lite DE Android"},
        {"uuid": "00ae8779-9a59-4f05-9bea-bd189703a0c4", "platform": "Lite FR Android"},
        {"uuid": "b05cc6df-8c8a-4b42-8953-79ff241ed22a", "platform": "Lite GB Android"},
        {"uuid": "ad026de8-9376-47cd-b3bb-fc093e2c9f59", "platform": "Lite ID Android"},
        {"uuid": "84643fa3-861b-4945-930d-bb18f7641dd1", "platform": "Lite US Android"},
        {"uuid": "bbc4610e-8357-4138-8971-9273d11a95cf", "platform": "Lite TR Android"},
        {"uuid": "7ba0c4f7-7fb4-4519-80f6-a141b09a7dd5", "platform": "Lite MX Android"},
        {"uuid": "62897d22-abf7-4e82-8883-49a56168745c", "platform": "Lite JP Android"},
        {"uuid": "233d9d02-2f46-4030-960f-86ec58fe3154", "platform": "Lite IN Android"},
        {"uuid": "468b9ee3-bbd3-453a-af93-743a87fc5a5c", "platform": "Lite CA iOS"},
        {"uuid": "3609cfe2-db83-4e0a-ae1e-da04d20157a9", "platform": "Lite DE iOS"},
        {"uuid": "bb6b523d-b3bf-4ff5-9cdc-076e0d2258ec", "platform": "Lite FR iOS"},
        {"uuid": "643023c6-92d1-4590-80dc-58f663f6f94d", "platform": "Lite GB iOS"},
        {"uuid": "292ec034-e5c6-4aa6-8584-e1dbd26003fe", "platform": "Lite ID iOS"},
        {"uuid": "9961d64e-c2a8-43de-b767-1bc1eefde123", "platform": "Lite US iOS"},
        {"uuid": "49ed9738-4009-4424-899c-4f22ee5bbd0d", "platform": "Lite TR iOS"},
        {"uuid": "aac75f2b-e203-4b00-9aa8-e98d5e37c000", "platform": "Lite MX iOS"},
        {"uuid": "85fb9b05-df0f-4567-bab4-2b5e1ad3fdab", "platform": "Lite JP iOS"},
        {"uuid": "93067a47-20e4-4514-ab06-fec31a70105e", "platform": "Lite IN iOS"},
        {"uuid": "95adc902-e523-4e92-a718-05547d4867cb", "platform": "Lite CA Windows"},
        {"uuid": "24ea2aea-b3c5-421b-89c2-0c325cf21ade", "platform": "Lite DE Windows"},
        {"uuid": "de280485-575e-4036-90fb-f0a205f9e5ad", "platform": "Lite FR Windows"},
        {"uuid": "7a9cc1a7-892d-44d8-aeee-f075c610fb6e", "platform": "Lite GB Windows"},
        {"uuid": "75287d1d-84e4-4161-a612-3145ef203cc8", "platform": "Lite ID Windows"},
        {"uuid": "5309de33-481f-46ca-a2b2-d9a14e1d6dbe", "platform": "Lite US Windows"},
        {"uuid": "59b235aa-567b-42fe-a64b-cda63212993e", "platform": "Lite TR Windows"},
        {"uuid": "8682c6c0-8077-4ea1-87a0-b26816489c25", "platform": "Lite MX Windows"},
        {"uuid": "6c9f6287-496d-4059-9ebd-0b276b51f222", "platform": "Lite JP Windows"},
        {"uuid": "db93547e-bcf3-48a2-86e5-7c92d90bc12d", "platform": "Lite IN Windows"},
        {"uuid": "966b584b-7224-48c7-a252-041256f18f65", "platform": "Lite CA MacOS"},
        {"uuid": "3be4d6f9-ae56-49b5-9250-62283ad258e8", "platform": "Lite DE MacOS"},
        {"uuid": "d1d373c6-3dde-49c4-9ac9-d0b09cffd2e6", "platform": "Lite FR MacOS"},
        {"uuid": "bc31ff67-0ade-4dd3-aafd-4be440e20a72", "platform": "Lite GB MacOS"},
        {"uuid": "0f769d4f-8e80-4bc4-9f8c-3280e85e1bbb", "platform": "Lite ID MacOS"},
        {"uuid": "68453649-e67d-4668-afe3-c1202232d1e8", "platform": "Lite US MacOS"},
        {"uuid": "26f3a3d4-2ad6-4b8d-abc4-0869c1ae42cc", "platform": "Lite TR MacOS"},
        {"uuid": "b658e632-8488-4177-b219-0f74ad75f4e0", "platform": "Lite MX MacOS"},
        {"uuid": "209ae0c7-482f-49cd-96f6-4a07166220a1", "platform": "Lite JP MacOS"},
        {"uuid": "3e27b211-5fe3-4cf4-9114-a67971a13769", "platform": "Lite IN MacOS"},
        {
            "uuid": "975f9edf-a0b4-4472-a44b-540192e8ce13",
            "platform": "Netproxy iOS (default)",
        },
        {
            "uuid": "210da616-6855-4dc0-9ed6-9296f9e8ae74",
            "platform": "Netproxy Android (default)",
        },
        {
            "uuid": "a23fa928-793e-4a32-a2ab-518610cefca5",
            "platform": "Netproxy MacOS (default)",
        },
        {
            "uuid": "5ccc3764-395a-4b3c-a009-463e71a910a0",
            "platform": "Netproxy Windows (default)",
        },
        {
            "uuid": "883f808d-771c-4da3-b798-915fcbe2da7d",
            "platform": "VPNLY iOS (default)",
        },
        {
            "uuid": "61e2961d-214c-4972-a1bc-e089ed86f6a8",
            "platform": "VPNLY Android (default)",
        },
        {
            "uuid": "089040d8-14d6-49ec-a4b7-a0773e70a777",
            "platform": "VPNLY Macos (default)",
        },
        {
            "uuid": "dfa1d8b7-2605-459b-97ff-b109b0c28997",
            "platform": "VPNLY Windows (default)",
        },
        {
            "uuid": "908c849a-1456-4c59-87e3-ae97ba79c809",
            "platform": "VPNLY Chrome (default)",
        },
        {
            "uuid": "359ff84d-d15f-4349-b45f-7a7339ed59b1",
            "platform": "VPNLY Firefox (default)",
        },
        {"uuid": "024e948f-97b1-41c0-9127-f4bd9cb956cf", "platform": "Planet iOS Rus"},
        {"uuid": "c379f9f8-b867-43f6-af16-43e545fbfd25", "platform": "Planet iOS Dark"},
        {"uuid": "70f3bb42-b3ee-48d3-b870-d30e34c8f27e", "platform": "Planet iOS Dark"},
        {
            "uuid": "795daf85-b159-4927-9586-6404c367e817",
            "platform": "VPNLY iOS (Astro)",
        },
        {
            "uuid": "bbf9aaf1-9d56-4886-8e68-b16c9da3cb47",
            "platform": "VPNLY iOS (Mars)",
        },
        {
            "uuid": "e2c37d51-00a3-4e1f-a41a-825837b2cf25",
            "platform": "VPNLY Android (Astro)",
        },
        {
            "uuid": "3c0706a5-9f63-4560-bf3d-c1cafedc9b73",
            "platform": "VPNLY Android (Mars)",
        },
        {"uuid": "2885ba7c-5958-46a5-b7ca-d8b3ac9be45f", "platform": "Planet iOS Rus"},
        {
            "uuid": "f3938da8-8143-41af-b8d2-c5c8aa533e17",
            "platform": "VPNLY iOS (Astro) – RU",
        },
        {
            "uuid": "bb5c7e34-4c3c-4dc6-b408-3315b0d3fbba",
            "platform": "VPNLY iOS (Mars) – RU",
        },
        {
            "uuid": "a94581c5-14ea-4311-8dcc-661bbe18f54d",
            "platform": "VPNLY Android (Astro) – RU",
        },
        {
            "uuid": "25fb6d1d-9cf8-4529-a52f-338685a006d7",
            "platform": "VPNLY Android (Mars) – RU",
        },
    ]
