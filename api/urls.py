from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('product-list/', views.product_list, name="products-list"),
    path('product-detail/<str:pk>/', views.product_detail, name="product-detail"),
    path('category-list/', views.category_list, name="category-list"),
    path('order-items/', views.order_items, name="order-items"),


]

