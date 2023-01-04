import os, json, requests, mock_data, time
from database_controller import Database_Controller
from dotenv import load_dotenv
from queue import Queue
from telegram_bot import Telegram_bot
load_dotenv()

'''
    @ 18/09/2022 jd
    How should the queue system work ? only important shit throw into queue
    script will check if nth in queue, then proceed to check user
        - check user using objects.get(), twitter_id of stalker and new_following
        queue should include add_new_user, should we have an api to communicate this ?
    i think dont need api, we can use database

    @ 17/09/2022 jd
    I think we need a queue system for user to add new users. It uses the same api key thus we need a script to check QUEUE
    Need to add this queue system into webserver

    @ 10/09/2022 jd
    create buffer for following. maybe track 50 most recent following instead of 20

    @ 08/09/2022 jd
    not sure but maybe can look into async functions
    maybe can add interface similar to typescript

    @ 6/9/2022 jd
    Twitter_Bot <-- inherits --- Database_Controller <-- inherits --- Http_Handler
'''



class Twitter_Bot(Database_Controller, Telegram_bot):

    bearer_token, api_key, api_key_secret, database_url = (
        os.getenv("BEARER_TOKEN"), 
        os.getenv('API_KEY'), 
        os.getenv('API_KEY_SECRET'), 
        os.getenv('DATABASE_URL')
    )

    base_url = 'https://api.twitter.com/2/'

    def __init__(self):
        Telegram_bot.__init__(self)
        self.queue = Queue()
        self.admin_id = '1334431789767479297'
        return

    def __str__(self):
        return f'Twitter bot : {self.get_bearer_token()}'

    def test_(self):
        data = Database_Controller.get_('twitter/')
        return data

    def get_bearer_token(self):
        return self.bearer_token

    def set_bearer_token(self, new_bearer_token: str) -> None:
        Twitter_Bot.bearer_token = new_bearer_token
        print(f'Successfully changed bearer token to {new_bearer_token}')
        return

    def request_new_bearer_token(self):
        '''
        @ 5/9/2022
        This is if bearer token expires. This function will automatically update .env file 
        '''
        credentials = (self.api_key, self.api_key_secret)

        pload = {
            'grant_type': 'client_credentials'
        }

        response_new_bearer_token = requests.post(f'https://api.twitter.com/oauth2/token', data=pload, auth=credentials)

        self.bearer_token = self.handle_res(response_new_bearer_token)['access_token']
        # Edit ENV file -> set new bearer token
        new_env_file_content = {}
        with open(".env", "r+") as f:
            for line in f.readlines():
                try:
                    key, value = line.split('=')
                    new_env_file_content[key] = value
                    if key == 'BEARER_TOKEN':
                        new_env_file_content[key] = self.bearer_token
                except ValueError:
                    # syntax error
                    pass
            f.close()

        with open(".env", "w") as f:
            for key in new_env_file_content:
                f.write(f'{key}={new_env_file_content[key]}\n')
            f.close()

        print(f'Successfully changed bearer token\nBEARER_TOKEN: {self.bearer_token}')

    # returns the user twitter_id
    def user_lookup_by_username(self, username:str):
        '''
        @ 5/9/2022
        It is better to use twitter_id instead of username because username is mutable
        '''
        route = f'users/by/username/{username}?user.fields=created_at,url,description'
        user_json = Twitter_Bot.get_(route=route)['data']
        print(user_json)
        return user_json

    # returns the user's following list
    def user_lookup_following(self, twitter_id:str, max_result:int) :
        '''

        @ 18/9/2022
        we using max_results=50 in our query, we will only use 20 to routinely check. 30 will be for buffer

        @ 5/9/2022
        It is better to use twitter_id instead of username because username is mutable
        returns you a list of people that you are following {name, username, id, created_at, url, description}
        '''
        route = f'users/{twitter_id}/following?max_results={max_result}&user.fields=created_at,url,description,public_metrics'
        user_json = self.get_(route=route)
        print('user info from api call : ',user_json.get('data'))

        return user_json.get('data')
    
    def add_twitter_user_database(self, user_list: list[str]):

        '''
        @ 8/9/2022 jd
        django will take care of repetitive users and it will ensure unique twitter_id inside the table

        ''' 
        
        user_list_complete = []
        following_list_complete = {}

        for each_user in user_list:
            user_list_complete.append(self.user_lookup_by_username(each_user))

        for each_user_complete in user_list_complete:
            each_user_twitter_id = each_user_complete['id']
            following_list_complete[each_user_twitter_id] = self.user_lookup_following(each_user_twitter_id,50)

        
        '''
            @ 08/09/22 jd 
            For testing, do not delete
        '''
        # user_list_complete = mock_data.user_test
        # following_list_complete = mock_data.following_test

        user_list_complete = json.dumps(user_list_complete)
        following_list_complete = json.dumps(following_list_complete)

        Database_Controller.twitter_add_new_stalker(self,user_list=user_list_complete, following_list=following_list_complete)

    def run_script(self):
    
        while True:

            stalker_list = Database_Controller.get_all_stalker(self)
            #test
            # stalker_list = ['1334431789767479297']
            #end test
            count = 0
            post_stalker_verification_list = []
            for stalker_id in stalker_list:
                print(count)
                count += 1
                attempt_number = 0
                while True:
                    
                    try:
                        '''
                        @ 22/9/2022 jd if-else statement for easier debug lol
                        '''
                        if (stalker_id == '1334431789767479297'):
                            print('attempt # ',attempt_number, ' on ', 'funnyGuyLarry (admin)')
                        else:
                            print('attempt # ',attempt_number, ' on ',stalker_id)
                        # remember to change back to 20
                        recent_20_following = self.user_lookup_following(stalker_id, 20)
                        #test
                        # recent_20_following = mock_data.recent_20_following
                        #end test
                        break
                    except Exception as e:
                        '''
                        @ jd 21/9/2022 I believe we can use the downtime to use the API for other functions - maybe we can explore after we get this shit done lol
                        there is no need for decorators
                        '''
                        attempt_number += 1
                        print(e,f'\n API rate limit reached - trying again in 30 seconds ...')
                        time.sleep(30)

                stalker_verification_info = { 
                    'stalker_id':stalker_id, 
                    'recent_20_following' :recent_20_following
                }
                post_stalker_verification_list.append(stalker_verification_info)

            Database_Controller.post_check_stalker_following(self,post_stalker_verification_list=json.dumps(post_stalker_verification_list))
            print('we are done iterating through the list !')
            time.sleep(60)


    


        
        


#  curl -u "K43UqwTkOceMPF6mjKJXBkNkJ:kLceQxVFxq3v9o6NazLIJkM48Gx2Js2oP3DjoWtgpV4piRCAOn"   --data 'grant_type=client_credentials'   'https://api.twitter.com/oauth2/token'
