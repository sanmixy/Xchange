# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0005_auto_20161217_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasource',
            old_name='port_avtive',
            new_name='port_active',
        ),
        migrations.AlterField(
            model_name='datasource',
            name='create_time',
            field=models.DateTimeField(help_text='create time', verbose_name=datetime.datetime(2016, 12, 17, 13, 10, 55, 968750, tzinfo=utc)),
        ),
    ]
