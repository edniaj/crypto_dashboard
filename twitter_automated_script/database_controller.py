from http_handler import Http_Handler
import os

'''
@ 19/9/2022
We are using class based method because different class has different base_url

@ 5/9/2022
This will directly interact with django backend server
'''
class Database_Controller(Http_Handler):

    bearer_token, database_url, base_url = (
        os.getenv("BEARER_TOKEN"), 
        os.getenv('DATABASE_URL'), 
        'http://localhost:8000/'
    )

    def __init__(self):
        return

    def twitter_add_new_stalker(self,**kwargs):
        
        success = Database_Controller.post_('twitter/add_new_stalker/', data={**kwargs})
        return success
    
    def get_all_stalker(self):

        stalker_list = Database_Controller.get_('twitter/get_all_stalker')
        return stalker_list['data']
    
    def post_check_stalker_following(self, **kwargs):
        # **kwargs twitter_id[]
        success = Database_Controller.post_('twitter/post_check_stalker_following/', data={**kwargs})
        pass
    


    
    
