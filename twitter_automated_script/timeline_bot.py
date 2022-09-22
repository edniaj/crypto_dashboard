import os, json, requests, mock_data, time
from http_handler import Http_Handler
from database_controller import Database_Controller
from dotenv import load_dotenv
from queue import Queue
from telegram_bot import Telegram_bot
load_dotenv()


class Timeline_bot(Http_Handler):


    base_url = 'https://api.twitter.com/2/'
    bearer_token, api_key, api_key_secret, database_url = (
        os.getenv("BEARER_TOKEN"), 
        os.getenv('API_KEY'), 
        os.getenv('API_KEY_SECRET'), 
        os.getenv('DATABASE_URL')
    )

    def __init__(self):
        pass

    def tweets_lookup_id(self,id:int):
        list_tweets = self.get_(f'lists/{id}/tweets')
        print(list_tweets)

