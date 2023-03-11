from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import *

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'product-list':'/product-list/',
        'product-detail':'/product-list/<str:pk>/',
        'category-list':'/category-list/',
        'category-detail':'/category-list/<str:pk>/',
        'order-items':'/order-items/',
        'checkout':'/checkout/'
    }
    return Response(api_urls)


@api_view(['GET','POST'])
def apiProducts(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])
def order_items(request):
    user = request.user
    print(user)
    cart, created = Order.objects.get_or_create(user=user)
    serializer = OrderSerializer(cart)
    return Response(serializer.data)

#@api_view(['GET', 'POST'])
#def product_list(request):
#    if request.method == 'GET':
#        products = Product.objects.all()
#        serializer = ProductSerializer(products, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        serializer = ProductSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#        return Response(serializer.data)



#@api_view(['GET', 'POST', 'DELETE'])
#def product_detail(request, pk):
#    try:
#        product = Product.objects.get(id=pk)
#    except Product.DoesNotExist:
#        return Response(status=404)
#
#    if request.method == 'GET':
#        product = Product.objects.get(id=pk)
#        serializer = ProductSerializer(product, many=False)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        serializer = ProductSerializer(instance=product, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#        return Response(serializer.data)
#
#    elif request.method == 'DELETE':
#        product.delete()
#        return Response('Deleted')






#@api_view(['GET','DELETE'])
#def category_detail(request,pk):
#    try:
#        category = Category.objects.get(id=pk)
#   except Category.DoesNotExist:
#        return Response(status=404)
#    if request.method == 'GET':
#        category = Category.objects.get(id=pk)
#       serializer = CategorySerializer(category, many=False)
#        return Response(serializer.data)
#    if request.method == 'DELETE':
#        category = Category.objects.get(id=pk)
#        category.delete()
#        return Response('Deleted')

#@api_view(['GET', 'POST'])
#def category_list(request):
#    if request.method == 'GET':
#        categories = Category.objects.all()
#        serializer = CategorySerializer(categories, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        serializer = CategorySerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#        return Response(serializer.data)




