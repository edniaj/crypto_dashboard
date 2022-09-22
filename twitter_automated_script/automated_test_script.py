import requests
import os
from twitter_bot import Twitter_Bot
from dotenv import load_dotenv
from telegram_bot import Telegram_bot
from timeline_bot import Timeline_bot
load_dotenv()


timeline_bot = Timeline_bot()
timeline_bot.tweets_lookup_id(84839422)