from django.contrib import admin

# Register your models here.
from datasource.models import DataSource, DatabaseSource, FTPSource

admin.site.register(DataSource)
admin.site.register(DatabaseSource)
admin.site.register(FTPSource)
