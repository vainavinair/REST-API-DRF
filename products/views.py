from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Products
from .serializers import ProductSerializer
from.permissions_authentications import AuthenticationMixin


def validate_description(attrs):
        name = attrs.get('name')
        description = attrs.get('description') or None
        if description is None:
            description = name
        return description


class ProductList(AuthenticationMixin, generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(AuthenticationMixin, generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        for item in serializer.validated_data:
            description = validate_description(item)
            item['description'] = description

        self.perform_create(serializer)
        return Response(serializer.data)


class ProductUpdate(AuthenticationMixin, generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        description = validate_description(serializer.validated_data)
        serializer.save(description=description)


class ProductDelete(AuthenticationMixin, generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data)

from rest_framework.authtoken.models import Token



