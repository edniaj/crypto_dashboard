# Generated by Django 4.1 on 2022-09-08 07:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_twitter_user_created_at_twitter_user_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stalking_logsheet',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 8, 7, 5, 33, 576623, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='twitter_user',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 8, 7, 5, 33, 528583, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='twitter_user',
            name='description',
            field=models.CharField(max_length=170, null=True),
        ),
    ]
