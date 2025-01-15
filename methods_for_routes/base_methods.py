import requests
from base_classes.data_in import DataIn
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import datetime
import os
from dotenv import load_dotenv
load_dotenv()


class AvailabilityRoutes:
    def __init__(self):
        self.time = time.time()

    def authenticate_free_user(self):
        """
            Performs Free user authorization.
        """
        authorization_user = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/login", data={
            "email": os.getenv("FREE_EMAIL"),
            "password": os.getenv("FREE_PASSWORD")
        })
        authorization = authorization_user.json()
        DataIn.token = authorization["data"]["token"]
        return DataIn.token

    def authenticate_premium_user(self):
        """
            Performs Premium user authorization.
        """
        authorization_user = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/login", data={
            "email": os.getenv("PREMIUM_EMAIL"),
            "password": os.getenv("PREMIUM_PASSWORD")
        })
        authorization = authorization_user.json()
        DataIn.token = authorization["data"]["token"]
        return DataIn.token

    def authenticate_premium_user_after_change_password(self):
        """
            Performs Premium user authorization.
        """
        authorization_user = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/login", data={
            "email": os.getenv("PREMIUM_EMAIL"),
            "password": os.getenv("NEW_PASSWORD_FOR_PREMIUM_USER")
        })
        authorization = authorization_user.json()
        DataIn.token = authorization["data"]["token"]
        return DataIn.token

    def check_authentication_token(self, token):
        """
            Will check the validity of the authorization token.
        """
        headers = {
            "Authorization": f"Bearer {token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"

        }
        check_token = requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/token/check", headers=headers)
        authentication_token = check_token.json()
        return authentication_token

    def change_password_back_premium_user(self):
        """
            Changes the Premium user's password.
        """
        base_methods = AvailabilityRoutes()
        DataIn.token = base_methods.authenticate_premium_user_after_change_password()
        headers = {
            "Authorization": f"Bearer {DataIn.token}",
            "Cache-Control": "no-cache"
        }
        requests.post(f"{os.getenv("PROTOCOL")}{os.getenv("DOMAIN")}/user/password/change", headers=headers, data={
            "password": os.getenv("OLD_PASSWORD_FOR_PREMIUM_USER"),
            "old_password": os.getenv("NEW_PASSWORD_FOR_PREMIUM_USER")
        })

    def get_current_time(self):
        current_time = datetime.datetime.now()
        time_part = str(current_time).split()[1]
        time_without_ms = time_part.split('.')[0]
        hours, minutes, seconds = map(int, time_without_ms.split(':'))
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds

    def decrypt_payload(self, payload, service):
        url = os.getenv("URL_ENCRYPTION")
        decrypt_payload = requests.post(url=url, data={
            "service": f"{service}",
            "payload": f"{payload}",
            "decrypt": 1
        })
        decrypted_payload = decrypt_payload.json()
        return decrypted_payload

    def send_mail(self):
        """
            Sends test results by email.
        """
        load_dotenv()
        with open("test_result.txt", encoding="utf-8") as result:
            report = result.read()
        if len(report) > 0:
            msg = MIMEMultipart()
            Login = os.getenv("login")
            Password = os.getenv("pass")
            to_email = os.getenv("to_email")
            msg['Subject'] = ("Result of test`s domains")
            msg['From'] = Login
            msg_body = ("Hi! Test`s result in the attachment file")
            msg.attach(MIMEText(msg_body, 'plain'))
            with open("test_result.txt", encoding="utf-8") as result:
                template = MIMEText(result.read())
            template.add_header('content-disposition', 'attachment', filename='test_result.txt')
            msg.attach(template)
            server = smtplib.SMTP_SSL('smtp.gmail.com:465')
            server.login(Login, Password)
            server.sendmail(Login, to_email, msg.as_string())
        else:
            print("The report is empty")

    def clear_data(self):
        """
            Сlears data in the test data file.
        """
        with open("test_result.txt", 'w', encoding="utf-8") as result:
            return result

