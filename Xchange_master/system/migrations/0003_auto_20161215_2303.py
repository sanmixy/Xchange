# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20161204_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginrecord',
            name='login_time',
            field=models.DateTimeField(help_text='login time', default=datetime.datetime(2016, 12, 15, 15, 3, 50, 562500, tzinfo=utc)),
        ),
    ]
