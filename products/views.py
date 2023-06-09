from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from.permissions_authentications import IsOwner


def validate_description(validated_data):
    name = validated_data.get('name')
    description = validated_data.get('description') or None
    if description is None:
        description = name
    return description

class ProductList( generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('category', 'user__username','user')
    ordering_fields = ('price',)
    search_fields = ('name', 'description','user__username','category')

class ProductDetail( generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    
    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     username = self.request.query_params.get('user')
    #     category = self.request.query_params.get('category')
    #     if username:
    #         username = User.objects.filter(username__contains=username).first()    
    #         queryset = queryset.filter(user=username)
    #     if category: 
    #         queryset = queryset.filter(category=category)
    #     return queryset

class ProductCreate( generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        description = validate_description(serializer.validated_data)
        serializer.save(description=description)

class ProductCreateMany( generics.CreateAPIView):
    queryset = Product.objects.all()
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


class ProductUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        IsOwner(request=self.request,obj=self.get_object())
        description = validate_description(serializer.validated_data)
        serializer.save(description=description)


class ProductDelete(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        IsOwner(request=self.request,obj=instance)
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data)
