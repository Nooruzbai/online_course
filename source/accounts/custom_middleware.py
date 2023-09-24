from django.utils.deprecation import MiddlewareMixin
import json

from rest_framework.reverse import reverse

from online_course import settings


class MoveJWTCookieIntoTheBody(MiddlewareMixin):
    """
    for Django Rest Framework JWT's POST "/token-refresh" endpoint --- check for a 'token' in the request.COOKIES
    and if, add it to the body payload.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if request.path in [reverse("token_verify"), reverse("rest_logout")] and settings.REST_AUTH["JWT_AUTH_COOKIE"] in request.COOKIES:
            if request.body != b'':
                data = json.loads(request.body)
                data['token'] = request.COOKIES[settings.REST_AUTH["JWT_AUTH_COOKIE"]]
                request._body = json.dumps(data).encode('utf-8')
            else:
                return f"The incoming request body must be set to an empty object."
        return None


class MoveJWTRefreshCookieIntoTheBody(MiddlewareMixin):
    """
    for Django Rest Framework JWT's POST "/token-refresh" endpoint --- check for a 'token' in the request.COOKIES
    and if, add it to the body payload.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if request.path in [reverse("token_refresh"), reverse("rest_logout")] and settings.REST_AUTH["JWT_AUTH_REFRESH_COOKIE"] in request.COOKIES:
            if request.body != b'':
                data = json.loads(request.body)
                data['refresh'] = request.COOKIES[settings.REST_AUTH["JWT_AUTH_REFRESH_COOKIE"]]
                request._body = json.dumps(data).encode('utf-8')
            else:
                print("The incoming request body must be set to an empty object.")
                return f"The incoming request body must be set to an empty object."
        return None

