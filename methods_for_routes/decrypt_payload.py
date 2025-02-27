import base64
import json
import os

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from dotenv import load_dotenv
load_dotenv()


class DecryptData:
    def decrypt_data(self, encrypted_value, iv, key):
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        padded_plaintext = cipher.decrypt(encrypted_value)
        plaintext = unpad(padded_plaintext, AES.block_size)
        return plaintext.decode('utf-8')

    def print_dict_values(self, data):
        if isinstance(data, str):
            data = json.loads(data)
        for key, value in data.items():
            if isinstance(value, dict):
                print(f"{key}:")
                DecryptData.print_dict_values(self, value)
            else:
                print(f"{key}: {value}")

    def main(self, payload):
        load_dotenv()
        key = base64.b64decode(os.getenv("KEY"))
        data = json.loads(payload)
        payload_value = data["payload"]
        encrypted_bytes = base64.b64decode(payload_value)

        data = json.loads(encrypted_bytes)

        iv_decoded = base64.b64decode(data['iv'])
        value_decoded = base64.b64decode(data['value'])

        decrypted_message = DecryptData.decrypt_data(self, value_decoded, iv_decoded, key)
        return decrypted_message

    def decrypt_from_api(self, payload: str, service_key: str) -> str:
        url = os.getenv("URL_ENCRYPTION")
        form_data = {"service": service_key, "payload": payload, "decrypt": "1"}
        response = requests.post(url, data=form_data)
        response_json = response.json()

        return response_json
