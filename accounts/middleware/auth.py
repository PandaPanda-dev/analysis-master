from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

class authMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if not request.user.is_authenticated:
            if request.path != '/login/' and request.path != '/logout/':
                return HttpResponseRedirect('/login/')
        return response
