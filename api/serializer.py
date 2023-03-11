from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id')



class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('id','name', 'price', 'category_name', 'category')
    def get_category_name(self, obj):
        category = obj.category
        return category.name if category else None



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
