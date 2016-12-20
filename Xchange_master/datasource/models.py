from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone

from system.models import Department, System


class DataSource(models.Model):
    source_types = (
        ('DB', 'database'),
        ('FTP', 'ftp'),
        ('SFTP', 'sftp')
    )
    alias = models.CharField(max_length=32, null=False, help_text='the name of datasource')
    create_time = models.DateTimeField(default=timezone.now(), help_text='create time')
    source_type = models.CharField(choices=source_types, max_length=5, help_text='specify the type of this datasource')
    host_active = models.CharField(max_length=16, default=None, null=True, help_text='ip address of this datasource')
    port_active = models.IntegerField(default=0, help_text='port of this datasource')
    host_standby = models.CharField(max_length=16, default=None, null=True, help_text='cluster settings')
    port_standby = models.IntegerField(default=0, help_text='the standby port')
    department = models.ForeignKey(Department)
    system = models.ForeignKey(System)
    username = models.CharField(max_length=64, default='', help_text='auth account')
    passcode = models.CharField(max_length=64, default='', help_text='auth passcode')

    def __unicode__(self):
        return self.alias

    class Meta:
        db_table = 'DATASOURCE'


class DatabaseSource(models.Model):
    database_types = (
        ('MYSQL', 'mysql'),
        ('SQLITE', 'sqlite'),
        ('ORACLE', 'oracle'),
        ('SQLSERVER', 'sqlserver')
    )
    datasource = models.ForeignKey(DataSource, on_delete=CASCADE)
    database_type = models.CharField(max_length=16, choices=database_types, help_text='type of database')
    database_name = models.CharField(max_length=32, null=True, default=None, help_text='database or service name')

    def __unicode__(self):
        return self.datasource.alias

    class Meta:
        db_table = 'DATABASE_SOURCE'


class FTPSource(models.Model):
    datasource = models.ForeignKey(DataSource, on_delete=CASCADE)

    def __unicode__(self):
        return self.datasource.alias

    class Meta:
        db_table = 'FTP_SOURCE'
