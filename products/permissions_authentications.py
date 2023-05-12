from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.exceptions import PermissionDenied


# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_authenticated:
#             return request.user.id == obj.id
#         return False
    
# class AuthenticationMixin:
#     # authentication_classes = [TokenAuthentication,SessionAuthentication ]
#     permission_classes = [IsAuthenticatedOrReadOnly]

class IsOwner(BasePermission):
    def __init__(self, request, obj):
        product = obj
        if request.user != product.user:
            raise PermissionDenied("You do not have permission to perform this action.")
