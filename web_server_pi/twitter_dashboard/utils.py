from twitter.models import Twitter_user, Stalking_logsheet
import datetime, json

def extract_user_list_req(req):
    '''
    @ 8/9/2022 jd
    returns query_dict into normal dict
    query_dict is meant for forms with multiple value (select) when you convert directly using .dict() you are getting 
    the iterator ? usually doesn't return a whole list thats why we need to write this shit lol
    '''
    query_dict = eval(f'req.{req.method}.lists()')
    dict_ = {}

    for tuple_ in query_dict:
        dict_[tuple_[0]] = json.loads(tuple_[1][0])
    
    return dict_
