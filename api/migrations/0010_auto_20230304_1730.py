# Generated by Django 3.2.16 on 2023-03-04 17:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_cart_cartitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='CartItem',
            new_name='OrderItem',
        ),
    ]
