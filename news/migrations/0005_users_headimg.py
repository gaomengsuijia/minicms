# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='headimg',
            field=models.FileField(default=datetime.datetime(2016, 8, 13, 3, 52, 49, 838000, tzinfo=utc), upload_to='./upload'),
            preserve_default=False,
        ),
    ]
