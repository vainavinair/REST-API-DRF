from rest_framework import serializers
from django.urls import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    product_url = serializers.HyperlinkedIdentityField(view_name="api-detail", lookup_field='id') 
    class Meta:
        model = Product
        fields = ('id', 'user', 'name', 'description', 'category', 'price', 'date_added', 'product_url')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
