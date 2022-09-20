import hashlib
from django.http import JsonResponse
from django.conf import settings


class AuthenticationMiddleware:
    """Middleware for request token validation."""

    def __init__(self, get_response):
        self.get_response = get_response

    def is_valid_token(self, token):
        """Validate token."""
        data = hashlib.md5(token.encode('utf-8'))
        if settings.HASH_STRING == data.hexdigest():
            return True
        return False

    def __call__(self, request):
        """
        If the request is not authenticated, then send invalid token json response
        """
        response = self.get_response(request)

        # get token from request params
        token = request.GET.get('token')
        # check if the token matches the one in the setting.py file
        is_valid = self.is_valid_token(token)
        if not is_valid:
            message = {
                'Authentication Failed': 'Invalid token'
            }
            return JsonResponse(message, status=400)
        return response
