# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0006_auto_20161217_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datasource',
            name='create_user',
        ),
        migrations.AlterField(
            model_name='datasource',
            name='create_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 12, 17, 13, 13, 26, 828125, tzinfo=utc), help_text='create time'),
        ),
    ]
