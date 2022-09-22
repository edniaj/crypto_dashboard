# Generated by Django 4.1 on 2022-09-05 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_alter_twitter_user_date_added_stalking_logsheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitter_user',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='twitter_user',
            name='description',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='twitter_user',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stalking_logsheet',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 5, 15, 17, 47, 233140, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='twitter_user',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 5, 15, 17, 47, 194135, tzinfo=datetime.timezone.utc)),
        ),
    ]