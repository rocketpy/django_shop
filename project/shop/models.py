from django.db import models


class Item(models.Model):
    prod_name = models.CharField(max_length=50)
    prod_descrip = models.TextField()
    price = models.IntegerField()
    img_url = models.ImageField()
    
    
"""
class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    # discount = models.IntegerField(default=0, )
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    # short_description = models.TextField(blank=True, null=True, default=None)
    # comments = models.TextField(blank=True, null=False, default=None)
    # created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return 'Order %s' % self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

"""
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Categories'

"""
class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/%Y%m%d', null=True)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.product.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
"""

"""
class ShoppingCart(models.Model):
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name
        
        
    def add_item(self, product, price):
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " is added !")
        else:
            print(product + " is already in the cart !")
    
    
    def remove_item(self, product):
        if product in self.items_in_cart:
            del self.item_in_cart[product]
            print(product + " is removed !")
        else:
            print(product + " is not in the cart !")
"""

#  for update use:  python manage.py makemigrations shop
# second command:  python manage.py migrate shop
