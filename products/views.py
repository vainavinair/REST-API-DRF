from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Products
from .serializers import ProductSerializer
from.permissions_authentications import AuthenticationMixin

from django_filters.rest_framework import DjangoFilterBackend

def validate_description(validated_data):
    name = validated_data.get('name')
    description = validated_data.get('description') or None
    if description is None:
        description = name
    return description

class ProductList(AuthenticationMixin, generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user']

class ProductCreate(AuthenticationMixin, generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        description = validate_description(serializer.validated_data)
        serializer.save(description=description)

class ProductCreateMany(AuthenticationMixin, generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        for validated_data in serializer.validated_data:
            description = validate_description(validated_data)
            validated_data['description'] = description
        serializer.save()




class ProductUpdate(AuthenticationMixin, generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        description = validate_description(serializer.validated_data)
        serializer.save(description=description)


class ProductDelete(AuthenticationMixin, generics.RetrieveDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data)
