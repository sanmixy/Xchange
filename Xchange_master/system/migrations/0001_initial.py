# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('department_name', models.CharField(max_length=64, help_text='the department of users')),
                ('is_center_department', models.BooleanField(help_text='judge the level of department', default=False)),
            ],
            options={
                'db_table': 'DEPARTMENT',
            },
        ),
        migrations.CreateModel(
            name='LoginRecord',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('login_time', models.DateTimeField(help_text='login time', default=datetime.datetime(2016, 12, 4, 5, 47, 36, 453125, tzinfo=utc))),
                ('user', models.ForeignKey(help_text='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'LOGIN_RECORD',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('system_name', models.CharField(max_length=64, help_text='the system of users, a system must be matched with a department')),
                ('department', models.ForeignKey(to='system.Department')),
            ],
            options={
                'db_table': 'SYSTEM',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('department', models.ForeignKey(null=True, to='system.Department', help_text="user's department")),
                ('system', models.ForeignKey(null=True, to='system.System', help_text="user's system")),
                ('user', models.ForeignKey(help_text='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'USER_PROFILE',
            },
        ),
    ]
