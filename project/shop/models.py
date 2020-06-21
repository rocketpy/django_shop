from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    
class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    category = models.ForeignKey(ProductCategory)
    description = models.TextField()

    def __str__(self):
        return 'Order %s' % self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
        
class Orders(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    # product ???
    
    def __str__(self):
        return self.first_name

    
class ProductCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Categories'


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products_images/%Y%m%d')

    def __str__(self):
        return '%s' % self.product.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class ShoppingCart(models.Model):
    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        if product not in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " is added !")
        else:
            print(product + " is already in the cart !")

    def remove_item(self, product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " is removed !")
        else:
            print(product + " is not in the cart !")
            

"""
# custom id field
import uuid
from django.db import models


class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # other fields
"""
            
#  for update use:  python manage.py makemigrations shop
# second command:  python manage.py migrate shop
