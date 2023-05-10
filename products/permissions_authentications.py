from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class AuthenticationMixin:
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]