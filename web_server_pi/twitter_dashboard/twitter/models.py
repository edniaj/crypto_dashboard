import datetime
import pytz

from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Twitter_user(models.Model):

    twitter_id = models.BigAutoField(null=False,unique=True, primary_key=True)
    name_alias = models.CharField(max_length=60, null=False)
    username = models.CharField(max_length=20, null=False)
    stalk_user = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=datetime.datetime.now(tz=pytz.timezone('Singapore')))
    created_at = models.DateTimeField(null=True)
    url = models.CharField(null=True,max_length=100)
    description = models.CharField(null=True,max_length=350)
    # def __str__(self):
    #     return f'name:{self.name_alias}\ntwitter_id:{self.twitter_id}\nstalking:{self.stalk_user}\nadded on {self.date_added}'
    
# related_name allows cleaner reverse lookup (Twitter_user.<related_name>_set.all())+ we got 2 foreign key,
class Stalking_logsheet(models.Model):
    stalking_twitter_id = models.ForeignKey(Twitter_user, on_delete=models.CASCADE, related_name='stalking_twitter_id')
    new_following_twitter_id = models.ForeignKey(Twitter_user, on_delete=models.CASCADE, related_name='new_following_twitter_id')
    date_added = models.DateTimeField(default=datetime.datetime.now(tz=pytz.timezone('Singapore')))
    
    def __str__(self):
        return f'{self.stalking_twitter_id} has followed {self.new_following_twitter_id} on {self.date_added}'
    
