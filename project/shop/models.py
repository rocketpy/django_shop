from django.db import models


class Item(models.Model):
    prod_name = models.CharField(max_length=50)
    prod_descrip = models.TextField()
    price = models.IntegerField()
    img_url = models.ImageField()


#  for update use:  python manage.py makemigrations shop
# second command:  python manage.py migrate shop
