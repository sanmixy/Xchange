"""Xchange_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from datasource import views

urlpatterns = [
    url(r'^dashboard$', views.datasource_view, name='datasource main page'),
    url(r'^department/all$', views.all_departments, name='all departments'),
    url(r'^system/filter$', views.system_with_depts, name='view system by department'),
    url(r'^push$', views.add_datasource, name='add a new datasource')
]
