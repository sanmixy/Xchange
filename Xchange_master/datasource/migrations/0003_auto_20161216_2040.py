# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0002_auto_20161214_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='database_name',
            field=models.CharField(default=None, help_text='database or service name', null=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='create_time',
            field=models.DateTimeField(help_text='create time', verbose_name=datetime.datetime(2016, 12, 16, 12, 40, 3, 406250, tzinfo=utc)),
        ),
    ]
