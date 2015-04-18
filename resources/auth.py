from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions, HTTP_HEADER_ENCODING
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import base64
from django.conf import settings

class FirstLoginToken(BaseAuthentication):
    def authenticate(self, request):
        admin = User.objects.all()
        if len(admin) > 0:
            return None

        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'basic':
            return None

        try:
            auth_parts = base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(':')
            userid, password = auth_parts[0], auth_parts[2]
        except (TypeError, UnicodeDecodeError):
            userid = None
        

        if userid == settings.FIRST_LOGIN_KEY:
            admin = User.objects.create_superuser('admin', '', password)
            admin.save()
            return (admin, None)


    def authenticate_header(self, request):
        return 'Basic realm="First Login"' 

