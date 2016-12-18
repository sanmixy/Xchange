from django.contrib.auth.admin import User
from django.db import models
from django.utils import timezone


class Department(models.Model):
    department_name = models.CharField(max_length=64, unique=True, help_text='the department of users')
    center_department = models.BooleanField(default=False, help_text='judge the level of department')

    def is_center(self):
        return self.is_center_department

    def __str__(self):
        return self.department_name

    class Meta:
        db_table = 'DEPARTMENT'


class System(models.Model):
    system_name = models.CharField(max_length=64, unique=True,
                                   help_text='the system of users, a system must be matched with a department')
    department = models.ForeignKey(Department)

    def __str__(self):
        return self.system_name

    class Meta:
        db_table = 'SYSTEM'


class UserProfile(models.Model):
    user = models.ForeignKey(User, help_text="user")
    department = models.ForeignKey(Department, null=True, help_text="user's department")
    system = models.ForeignKey(System, null=True, help_text="user's system")

    def __str__(self):
        return self.user.username

    def is_department_user(self):
        return self.department and not self.system

    def is_system_user(self):
        return self.department and self.system

    class Meta:
        db_table = "USER_PROFILE"


class LoginRecord(models.Model):
    user = models.ForeignKey(User, help_text='user')
    login_time = models.DateTimeField(default=timezone.now(), help_text='login time')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "LOGIN_RECORD"
