from django.shortcuts import render, get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.decorators import api_view

from .models import Products
from .serializers import ProductSerializer
from.permissions_authentications import AuthenticationMixin


# @api_view(['GET'])
# def home(request):
#     data = Products.objects.all()
#     serializer = ProductSerializer(data, many=True)
#     return Response(serializer.data)

def validate_decription(serializer):
    name = serializer.validated_data.get('name')
    description = serializer.validated_data.get('description') or None
    if description is None:
        description = name
    return description


class ProductList(AuthenticationMixin, generics.ListAPIView):
# class ProductList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description') or None
        if description is None:
            description = name
        serializer.save(description=description)

class ProductUpdate(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        description = validate_decription(serializer)
        serializer.save(description=description)


class ProductDelete(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data)