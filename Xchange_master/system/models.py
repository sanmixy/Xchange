from django.contrib.auth.admin import User
from django.db import models
from django.utils import timezone


class LoginRecord(models.Model):
    user = models.ForeignKey(User)
    login_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "LOGIN_RECORD"
