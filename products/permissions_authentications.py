from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class AuthenticationMixin:
    authentication_classes = [TokenAuthentication,SessionAuthentication ]
    permission_classes = [IsAuthenticated]