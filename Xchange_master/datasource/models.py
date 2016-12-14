from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from system.models import Department, System


class DataSource(models.Model):
    source_types = (
        ('DB', 'database'),
        ('FTP', 'ftp'),
        ('SFTP', 'sftp')
    )
    create_user = models.ForeignKey(User, help_text='the user who create this datasource')
    create_time = models.DateTimeField(timezone.now(), help_text='create time')
    source_type = models.CharField(choices=source_types, max_length=5, help_text='specify the type of this datasource')
    host_active = models.GenericIPAddressField(protocol='both', unpack_ipv4=False,
                                               help_text='ip address of this datasource')
    port_avtive = models.IntegerField(default=0, help_text='port of this datasource')
    host_standby = models.GenericIPAddressField(default='0.0.0.0', protocol='both', unpack_ipv4=False,
                                                help_text='cluster settings')
    port_standby = models.IntegerField(default=0, help_text='the standby port')
    department = models.ForeignKey(Department)
    system = models.ForeignKey(System)

    def __str__(self):
        return self.host

    class Meta:
        db_table = 'DATASOURCE'
