# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 11:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('therapydemo', '0008_auto_20160829_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_date_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 29, 11, 56, 41, 61942, tzinfo=utc)),
        ),
    ]
