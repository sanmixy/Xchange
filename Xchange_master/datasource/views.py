# Create your views here.
import base64
import json

from django.core import serializers
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from datasource.Cipher import encode
from datasource.models import DataSource, DatabaseSource
from system.models import Department, System
from system.views import person_info


def datasource_view(request):
    return render(request, 'datasource/page/datasource.html', person_info(request))


@csrf_exempt
def all_departments(request):
    all_depts = {'result': True,
                 'data': serializers.serialize('json', Department.objects.all())}
    return HttpResponse(json.dumps(all_depts), content_type='application/json')


@csrf_exempt
def system_with_depts(request):
    dept_id = request.POST.get('department')
    if dept_id:
        all_systems = {'result': True,
                       'data': serializers.serialize('json', System.objects.filter(Q(department_id=dept_id)))}
    else:
        all_systems = {'result', False}
    return HttpResponse(json.dumps(all_systems), content_type='application/json')


@csrf_exempt
def add_datasource(request):
    datasource_processor = {
        'DB': database_processor
    }
    alias = request.POST.get('alias', None)
    department_id = request.POST.get('department', None)
    system_id = request.POST.get('system', None)
    type = request.POST.get('type', None)
    database_type = request.POST.get('database_type', None)
    host_active = request.POST.get('host_active', None)
    port_active = request.POST.get('port_active', None)
    database_name = request.POST.get('database_name', None)
    username = request.POST.get('username', None)
    passcode = base64.b64encode(encode(request.POST.get('passcode', None)))
    output = {
        'result': datasource_processor[type](alias, department_id, system_id, database_type, host_active, port_active,
                                             database_name, username, passcode)}
    return HttpResponse(json.dumps(output), content_type='application/json')


@transaction.atomic
def database_processor(alias, department_id, system_id, database_type, host_active, port_active, database_name,
                       username, passcode):
    try:
        datasource = DataSource(alias=alias, department_id=department_id, system_id=system_id,
                                host_active=host_active, port_active=port_active, username=username,
                                passcode=passcode)
        datasource.save()
        database_source = DatabaseSource(database_type=database_type,
                                         database_name=database_name)
        database_source.save()
        return True
    except Exception:
        return False
