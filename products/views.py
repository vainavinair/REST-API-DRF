from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Products

@api_view(['GET'])
def home(request):
    data = Products.objects.all()
    serializer = ProductSerializer(data, many=True)
    return Response(serializer.data)