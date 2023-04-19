from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),

    path('product-list/', views.productsList, name="products-list"),

    path('product-list/<str:pk>/', views.productDetail, name="product-detail"),

    path('category-list/', views.category_list, name="category-list"),

    path('category-list/<str:pk>/', views.category_detail, name="category-detail"),

   # path('order-items/', views.order_items, name="order-items"), 

    path('category-products/<str:pk>/', views.category_products, name="category-products"),

    #path('orders/', views.OrderList.as_view(), name='order-list'),

    path('orders/', views.orderList, name='order-list'),

    path('login/', views.login), 



#    path('orderList/', views.OrderList.as_view(), name='') 
]


