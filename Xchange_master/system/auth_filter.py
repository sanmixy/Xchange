from django.http import HttpResponseRedirect


class AuthFilter(object):
    def process_request(self, request):
        if request.path != '/system/auth':
            if 'person' not in request.session:
                return HttpResponseRedirect('/system/auth')
