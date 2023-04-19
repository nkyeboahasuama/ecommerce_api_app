from django.db import models
from django.contrib.auth.models import User
from django.db.models import DateTimeField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')


    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    order_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.id}'

    @property
    def total(self):
        total = 0
        for item in self.items.all():
            total += item.subtotal
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return str(self.order)

    @property
    def subtotal(self):
        return self.product.price * self.quantity



    