# Create your views here.
from django.shortcuts import render

from system.views import person_info


def datasource_view(request):
    return render(request, 'datasource/page/datasource.html', person_info(request))
