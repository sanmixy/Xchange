import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def login_view(request):
    return render(request, 'system/page/login.html')


def session_processor(request, person):
    request.session['status'] = True
    request.session['person'] = person.username
    request.session['person_id'] = person.id


@csrf_exempt
def sign_in(request):
    username = request.POST.get('username', None)
    passcode = request.POST.get('passcode', None)
    person = authenticate(username=username, password=passcode)
    if person and person.is_active:
        login(request, person)
        session_processor(request, person)
        return HttpResponse(json.dumps({'result': True}), content_type='application/json')
    return HttpResponse(json.dumps({'result': False}), content_type='application/json')


def dashboard(request):
    return render(request, 'system/page/dashboard.html', person_info(request))


def person_info(request):
    session = request.session
    try:
        person = User.objects.get(id=session.get('person_id', '0'))
    except User.DoesNotExist:
        person = ''
    return {'person': person, 'status': session.get('status', False)}


@csrf_exempt
def sign_out(request):
    session = request.session
    if 'person' in request.session:
        if session.get('status', False):
            try:
                del request.session['person']
                del request.session['person_id']
                request.session['status'] = False
            except KeyError:
                pass
    return HttpResponse(json.dumps({'result': True}), content_type='application/json')
