# Generated by Django 4.1 on 2022-09-21 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_alter_stalking_logsheet_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stalking_logsheet',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 21, 13, 43, 16, 831559, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='twitter_user',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 21, 13, 43, 16, 787558, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='twitter_user',
            name='description',
            field=models.CharField(max_length=350, null=True),
        ),
    ]