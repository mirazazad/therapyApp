# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 09:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('therapydemo', '0004_auto_20160829_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_date_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 29, 9, 23, 36, 448446, tzinfo=utc)),
        ),
    ]
