# Generated by Django 4.1 on 2022-09-05 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twitter_user',
            fields=[
                ('twitter_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('name_alias', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=20)),
                ('stalk_user', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2022, 9, 5, 6, 16, 19, 901958, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
