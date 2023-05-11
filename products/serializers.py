from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'user', 'name', 'description', 'category', 'price', 'date_added')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
