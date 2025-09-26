# website/serializers.py
from rest_framework import serializers
from .models import Products  # Import your Products model

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'stock']  # Include all fields