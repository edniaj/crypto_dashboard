import os
import json
import requests
import time
from dotenv import load_dotenv
load_dotenv()


class Telegram_bot:


    def __init__(self):
        self.telegram_api_key = os.environ.get('TELEGRAM_API_KEY')
        self.chat_id = os.environ.get('TELEGRAM_CHAT_ID')
        self.base_url = 'https://api.telegram.org/bot'

    def send_telegram_message(self, message):
        print('message : ', message)
        requests.post(f'https://api.telegram.org/bot{self.telegram_api_key}/sendMessage?chat_id={self.chat_id}&text={message}')
