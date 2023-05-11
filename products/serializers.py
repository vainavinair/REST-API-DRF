from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Products
        fields = ('id', 'user', 'name', 'description', 'price', 'image')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
