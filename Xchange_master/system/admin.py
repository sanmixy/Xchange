from django.contrib import admin

# Register your models here.
from system.models import Department, System

admin.site.register(Department)
admin.site.register(System)
