from django.shortcuts import render

def dashboard(request):
    return render(request, 'system/page/base.html')

def login_view(request):
    return render(request, 'system/page/login.html')