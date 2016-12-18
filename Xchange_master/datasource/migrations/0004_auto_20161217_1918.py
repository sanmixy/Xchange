# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0003_auto_20161216_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseSource',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('database_type', models.CharField(max_length=16, choices=[('MYSQL', 'mysql'), ('SQLITE', 'sqlite'), ('ORACLE', 'oracle'), ('SQLSERVER', 'sqlserver')], help_text='type of database')),
                ('database_name', models.CharField(max_length=32, default=None, null=True, help_text='database or service name')),
            ],
            options={
                'db_table': 'DATABASE_SOURCE',
            },
        ),
        migrations.CreateModel(
            name='FTPSource',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
            options={
                'db_table': 'FTP_SOURCE',
            },
        ),
        migrations.RemoveField(
            model_name='datasource',
            name='database_name',
        ),
        migrations.AddField(
            model_name='datasource',
            name='alias',
            field=models.CharField(max_length=32, default=datetime.datetime(2016, 12, 17, 11, 18, 12, 984375, tzinfo=utc), help_text='the name of datasource'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datasource',
            name='passcode',
            field=models.CharField(max_length=64, default='', help_text='auth passcode'),
        ),
        migrations.AddField(
            model_name='datasource',
            name='username',
            field=models.CharField(max_length=64, default='', help_text='auth account'),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='create_time',
            field=models.DateTimeField(help_text='create time', verbose_name=datetime.datetime(2016, 12, 17, 11, 18, 2, 31250, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='ftpsource',
            name='datasource',
            field=models.ForeignKey(to='datasource.DataSource'),
        ),
        migrations.AddField(
            model_name='databasesource',
            name='datasource',
            field=models.ForeignKey(to='datasource.DataSource'),
        ),
    ]
