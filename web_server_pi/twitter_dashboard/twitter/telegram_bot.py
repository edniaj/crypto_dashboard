import os
import json
import requests
import time


class Telegram_bot:

    def __init__(self):
        self.telegram_api_key = '5589789589:AAHemFviNSRITZiEMGWbFXvslgrA2QYgjGo'
        self.chat_id = -1001632547386
        self.base_url = 'https://api.telegram.org/bot'

    def send_telegram_message(self, message):
        print('message : ', message)
        requests.post(f'https://api.telegram.org/bot{self.telegram_api_key}/sendMessage?chat_id={self.chat_id}&text={message}')
