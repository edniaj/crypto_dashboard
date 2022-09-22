import requests
import os
from twitter_bot import Twitter_Bot
from dotenv import load_dotenv
from telegram_bot import Telegram_bot
from timeline_bot import Timeline_bot
load_dotenv()

# print(os.getenv('API_KEY_SECRET'))
# Example of how to post with modified header + data
# headers = {
#   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
# }
# pload = {'key':'value'}
# r = requests.post('https://URL', data=pload, headers=headers)


# Bot uses config from .env file
twitter_bot = Twitter_Bot()
# twitter_bot.add_twitter_user_database(['FollowMyEyesDAO', 'wassiecapital', 'DefiIgnas', 'TaikiMaeda2', '3azima85'])
# twitter_bot.user_lookup_by_username('funnyGuyLarry')
twitter_bot.run_script()

