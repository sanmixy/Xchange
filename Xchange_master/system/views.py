import json

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def login_view(request):
    return render(request, 'system/page/login.html')


def session_processor(request, person):
    request.session['status'] = True
    request.session['username'] = person.username


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
    return HttpResponse(json.dumps(["hello"]), content_type='application/json')
