from dotenv import load_dotenv
import requests

class Http_Handler():

    def __init__(self):
        return

    def handle_res(self,res):
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception(f'status code : {res.status_code}\ncontent : {res.reason}')

    @classmethod
    def get_(cls, route,**kwargs):
        headers={'Authorization': f'Bearer {cls.bearer_token}'}
        get_request = requests.get(f'{cls.base_url}{route}', headers=headers, **kwargs)
        return cls.handle_res(cls,get_request)

    @classmethod
    def post_(cls, route, **kwargs):
        headers={'Authorization': f'Bearer {cls.bearer_token}'}
        post_request = requests.post(f'{cls.base_url}{route}', headers=headers, **kwargs)
        return cls.handle_res(cls, post_request)

