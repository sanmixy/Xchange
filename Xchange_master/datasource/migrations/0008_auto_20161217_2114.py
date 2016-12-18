# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0007_auto_20161217_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 17, 13, 14, 10, 390625, tzinfo=utc), help_text='create time'),
        ),
    ]
