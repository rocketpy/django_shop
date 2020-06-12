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


#  for update use:  python manage.py makemigrations shop
# second command:  python manage.py migrate shop
