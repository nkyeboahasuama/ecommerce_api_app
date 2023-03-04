from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ('product','quantity')


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('items', 'user')
