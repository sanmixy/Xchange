# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasource',
            old_name='host',
            new_name='host_active',
        ),
        migrations.RenameField(
            model_name='datasource',
            old_name='port',
            new_name='port_avtive',
        ),
        migrations.AddField(
            model_name='datasource',
            name='host_standby',
            field=models.GenericIPAddressField(help_text='cluster settings', default='0.0.0.0'),
        ),
        migrations.AddField(
            model_name='datasource',
            name='port_standby',
            field=models.IntegerField(help_text='the standby port', default=0),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='create_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 12, 14, 13, 54, 33, 921875, tzinfo=utc), help_text='create time'),
        ),
    ]
