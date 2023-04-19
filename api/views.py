from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework import generics, permissions, status
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'product-list':'/product-list/',
        'product-detail':'/product-list/<str:pk>/',
        'category-list':'/category-list/',
        'category-detail':'/category-list/<str:pk>/',
        'category-products': '/category-products/<str:pk>/',
        'order-items':'/order-items/',
        'checkout':'/checkout/'
    }
    return Response(api_urls)

@api_view(['GET','POST'])
def productsList(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'POST', 'DELETE'])
def productDetail(request, pk):
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


@api_view(['GET','DELETE'])
def category_detail(request,pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
            return Response(status=404)
    if request.method == 'GET':
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
    if request.method == 'DELETE':
        category = Category.objects.get(id=pk)
        category.delete()
        return Response('Deleted')

@api_view(['GET', 'POST'])
def category_products(request,pk):  
    if request.method == 'GET':
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        category_products = category.products.all()
        serializer = CategorySerializer(category_products, many=True)
        return Response(serializer.data) 

@api_view(['POST'])
def login(request):
    username = request.data.get('username') 
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    print(user)
    
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        print(user)
        return Response({'token': token.key, 'user': serializer.data})
    else:
        print(user)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orderList(request):
    user = request.user
    print(user)
    if user.is_authenticated:
        orders = Order.objects.filter(user=user)
        data = {
            'user': UserSerializer(user).data,
            'orders': OrderSerializer(orders, many=True).data
        }
        return Response(data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

        
 






#class OrderList(generics.ListAPIView):
#    permission_classes = [permissions.IsAuthenticated]
#
#    def get_queryset(self, request):
#        username = request.data.get('username')
#        password = request.data.get('password')
#        user = authenticate(username=username, password=password)
#        print(user) 
#        queryset = Order.objects.filter(user=user)
#        return queryset
        
#    serializer_class = OrderSerializer














#@api_view(['GET', 'POST'])
#def order_items(request):
#    if request.method == 'GET':
#        order = Order.objects.all()
#        serializer = OrderSerializer(order, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        data = request.data
#        serializer = OrderSerializer(data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)




#class OrderList(generics.ListCreateAPIView):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer


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



#class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer

#class CategoryList(generics.ListCreateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer

#class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer










