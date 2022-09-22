from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from utils import extract_user_list_req
from twitter.models import Twitter_user, Stalking_logsheet
import datetime
from queue import Queue
import json
from .telegram_bot import Telegram_bot
'''
README

    @22/9/2022
    Maybe add feature to stalk user (once user has either been created or not... i think this can be a potential bug)

    @18/9/2022
    Remember to change limit_size to 20 instead of 5

    @ 17/9/2022 
    We need a queue system for automation script so that we can use the same API key to either add new users into stalker or automate track

'''

queue_automation_system = Queue()

def default(req):
    data = {'success':str(datetime.datetime.now())}
    return JsonResponse(data)

def all_twitter_info(req):


    limit_size = 200    

    stalking_logsheet = Stalking_logsheet.objects.all().order_by('-date_added')[:limit_size]
    stalking_logsheet_json = parse_logsheet_queryset_into_json(stalking_logsheet)

    users_in_logsheet = {}

    for each_query in stalking_logsheet:

        stalker_id = each_query.stalking_twitter_id.twitter_id 
        new_following_id = each_query.new_following_twitter_id.twitter_id

        '''
        @ 16/9/2022 jd
            We will use user's twitter_id as key do that its O(1) operation in the frontend
            You cannot serialize an object, you can only serialize a list / query_set
        '''

        if not(users_in_logsheet.get(stalker_id, False)):
            users_in_logsheet[stalker_id] = parse_model_into_json(each_query.stalking_twitter_id)

        if not(users_in_logsheet.get(new_following_id, False)):
            users_in_logsheet[new_following_id] = parse_model_into_json(each_query.new_following_twitter_id)

    # print(stalking_logsheet_json)

    return JsonResponse({
        'twitter_users': users_in_logsheet,
        'stalking_logsheet': stalking_logsheet_json
    })


# @csrf_exempt
def add_new_stalker(req):

    req_json = extract_user_list_req(req)

    user_list = req_json['user_list']
    following_list = req_json['following_list']  
    # print('user_list : \n',user_list)
    # print('following_list : \n',following_list)
    '''
    @ 8/9/2022 jd
    bulk_create will add all these users in 1 query. ignore_conflicts=True will prevent repetition
    '''
    twitter_user_list = []
    for each_user in user_list:
        twitter_user_list.append(Twitter_user(
            twitter_id=each_user['id'],
            url=each_user['url'],
            created_at = datetime.datetime.fromisoformat(each_user['created_at'][:13]),
            name_alias=each_user['name'],
            username=each_user['username'],
            description=each_user['description'],
            stalk_user = True
        ))
    Twitter_user.objects.bulk_create(twitter_user_list, ignore_conflicts=True)

    twitter_user_following_list = []
    stalking_logsheet_list = []
    for stalker_twitter_id in following_list:
        
        stalker_twitter_user = Twitter_user.objects.get(twitter_id=stalker_twitter_id)

        for each_user in following_list[stalker_twitter_id]:
            new_following_user = Twitter_user(
                twitter_id=each_user['id'],
                url=each_user['url'],
                created_at = datetime.datetime.fromisoformat(each_user['created_at'][:13]),
                name_alias=each_user['name'],
                username=each_user['username'],
                description=each_user['description'][:170],
            )

            twitter_user_following_list.append(new_following_user)

            stalking_logsheet_list.append(Stalking_logsheet(
                stalking_twitter_id = stalker_twitter_user,
                new_following_twitter_id = new_following_user
            ))


    Twitter_user.objects.bulk_create(twitter_user_following_list, ignore_conflicts=True)
    Stalking_logsheet.objects.bulk_create(stalking_logsheet_list, ignore_conflicts=True)

    return JsonResponse({'success':'yes'})

def get_all_stalker(req):
    stalker_users = Twitter_user.objects.values('twitter_id').filter(stalk_user=True)
    stalker_list = []
    for user in stalker_users:
        # @19/9/2022 JD number is too long, not safe for js (frontend)
        stalker_list.append(str(user['twitter_id']))
    
    return JsonResponse({'data': stalker_list})

def post_check_stalker_following(req):
    # stalker_verification_list = extract_user_list_req(req)
    data = req.POST.get('post_stalker_verification_list')
    stalker_verification_list = json.loads(data)
    telegram_bot = Telegram_bot()

    '''
    @ 21/9/2022 jd
    we have issues, repetition inside the logsheet -_-

    @ 20/9/2022 jd 
    convert queryset into dict so that we can access Twitter_User model with O(1) operation. We also do not want to spam call the database
    '''
    stalker_database = Twitter_user.objects.filter(stalk_user=True)
    stalker_database_dict = {}

    for each_stalker in stalker_database:
        stalker_database_dict[str(each_stalker.twitter_id)] = each_stalker

    logsheet_database_recent_50 = Stalking_logsheet.objects.select_related('stalking_twitter_id').filter(stalking_twitter_id__stalk_user=True)
    '''
    @ 21/9/2022 jd We store tuple of (stalker_id, new_following_id) inside the set, we will use the set to determine if new following has been logged
    '''
    logsheet_database_set= set()

    for logsheet in logsheet_database_recent_50:
        logsheet_database_set.add(( str(logsheet.stalking_twitter_id.twitter_id), str(logsheet.new_following_twitter_id.twitter_id)))

    for stalker in stalker_verification_list:
        # stalker {stalker_id: str , recent_20_following: api_data[]}
        
        stalker_name = stalker_database_dict.get(stalker.get('stalker_id')).username
        print(f'stalker_name : {stalker_name}')

        add_new_user_list = []
        add_new_logsheet_list = []
        for new_following in stalker['recent_20_following']:
            check_this_tuple = (stalker.get('stalker_id'), str(new_following.get('id')) )

            if check_this_tuple not in logsheet_database_set :

                new_user = Twitter_user(
                    twitter_id=new_following.get('id'),
                    url=new_following.get('url'),
                    created_at = datetime.datetime.fromisoformat(new_following.get('created_at')[:13]),
                    name_alias=new_following.get('name'),
                    username=new_following.get('username'),
                    description=new_following.get('description'),
                    stalk_user = False
                )

                new_logsheet =  Stalking_logsheet( 
                    stalking_twitter_id = stalker_database_dict[stalker.get('stalker_id')],
                    new_following_twitter_id = new_user
                )
                add_new_user_list.append(new_user)
                add_new_logsheet_list.append(new_logsheet)
                

                new_following_username = new_following.get('username')
                new_following_url = new_following.get('url', None)
                new_following_follower_count = new_following.get('public_metrics')['followers_count']
                
                if new_following_follower_count < 500:
                    new_following_follower_count_tag = '🔴'
                elif new_following_follower_count < 5000:
                    new_following_follower_count_tag = '🟡'
                else:
                    new_following_follower_count_tag = '🟢'

                message = f'@{stalker_name} has followed https://twitter.com/{new_following_username}\nFollower : {new_following_follower_count} {new_following_follower_count_tag}  \ Website: {new_following_url}'
                telegram_bot.send_telegram_message(message)

        # @20/9/2022 JD User might have already been registered. We still want to add into the logsheet. 
        Twitter_user.objects.bulk_create(add_new_user_list, ignore_conflicts=True)
        Stalking_logsheet.objects.bulk_create(add_new_logsheet_list)


    return JsonResponse({'data':'success'})

#utils 
def parse_model_into_json(model):
    model_serialized = serializers.serialize('json',[model])
    model_json = json.loads(model_serialized)
    return model_json[0]['fields']

def parse_logsheet_queryset_into_json(model):
    
    model_serialized = serializers.serialize('json', model)
    model_json = json.loads(model_serialized)

    model_list_only_display_fields = []

    for each_model in model_json:
        each_model['fields']['stalking_twitter_id'] = str(each_model['fields']['stalking_twitter_id'])
        each_model['fields']['new_following_twitter_id'] = str(each_model['fields']['new_following_twitter_id'])
        model_list_only_display_fields.append(each_model['fields'])
    
    return model_list_only_display_fields