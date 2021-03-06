from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id', 'unit_price', 'category', 'name',
                  'variety', 'avail_weight', 'quantity']
