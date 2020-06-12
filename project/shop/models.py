from django.db import models


class Item(models.Model):
    prod_name = models.CharField(max_length=50)
    prod_descrip = models.TextField()
    price = models.IntegerField()
    img_url = models.ImageField()
    
    
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
