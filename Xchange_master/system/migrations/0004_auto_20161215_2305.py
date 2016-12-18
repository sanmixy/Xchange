# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20161215_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='is_center_department',
            new_name='center_department',
        ),
        migrations.AlterField(
            model_name='loginrecord',
            name='login_time',
            field=models.DateTimeField(help_text='login time', default=datetime.datetime(2016, 12, 15, 15, 5, 36, 296875, tzinfo=utc)),
        ),
    ]
