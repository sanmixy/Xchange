from django.http import HttpResponseRedirect

paths = [
    '/'
]


class AuthFilter(object):
    @staticmethod
    def process_request(request):
        if request.path in paths:
            if 'username' not in request.session:
                return HttpResponseRedirect('/system/auth')
