# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20161204_1347'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(verbose_name=datetime.datetime(2016, 12, 4, 5, 47, 47, 562500, tzinfo=utc), help_text='create time')),
                ('source_type', models.CharField(choices=[('DB', 'database'), ('FTP', 'ftp'), ('SFTP', 'sftp')], max_length=5, help_text='specify the type of this datasource')),
                ('host', models.GenericIPAddressField(help_text='ip address of this datasource')),
                ('port', models.IntegerField(help_text='port of this datasource', default=0)),
                ('create_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, help_text='the user who create this datasource')),
                ('department', models.ForeignKey(to='system.Department')),
                ('system', models.ForeignKey(to='system.System')),
            ],
            options={
                'db_table': 'DATASOURCE',
            },
        ),
    ]
