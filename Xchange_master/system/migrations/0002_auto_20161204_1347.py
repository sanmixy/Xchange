# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginrecord',
            name='login_time',
            field=models.DateTimeField(help_text='login time', default=datetime.datetime(2016, 12, 4, 5, 47, 47, 562500, tzinfo=utc)),
        ),
    ]
