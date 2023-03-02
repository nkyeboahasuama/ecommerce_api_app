from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer, CategorySerializer
from .models import Product, Category

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'product-list':'/product-list/',
        'product-detail':'/product-detail/',
        'category-list':'/category-list/'
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    

@api_view(['GET', 'POST', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        return Response('Deleted')


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)





