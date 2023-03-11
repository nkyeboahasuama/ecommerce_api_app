from django.db import models
from django.contrib.auth.models import User


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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

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
        return str(self.cart)

    @property
    def subtotal(self):
        return self.product.price * self.quantity
    


