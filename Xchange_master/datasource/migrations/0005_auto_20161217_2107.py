# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0004_auto_20161217_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='create_time',
            field=models.DateTimeField(help_text='create time', verbose_name=datetime.datetime(2016, 12, 17, 13, 7, 50, 937500, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='host_active',
            field=models.CharField(max_length=16, default=None, null=True, help_text='ip address of this datasource'),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='host_standby',
            field=models.CharField(max_length=16, default=None, null=True, help_text='cluster settings'),
        ),
    ]
