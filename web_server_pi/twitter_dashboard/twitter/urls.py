from django.urls import path
from . import route

urlpatterns=[
    path('', route.default),
    path('all_twitter_info/', route.all_twitter_info),
    path('add_new_stalker/', route.add_new_stalker),
    path('get_all_stalker/', route.get_all_stalker),
    path('post_check_stalker_following/', route.post_check_stalker_following)
]