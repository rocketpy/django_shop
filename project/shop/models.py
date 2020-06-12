from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    name = models.CharField(max_length=20)
    price = models.IntegerField()


#  for update use:  python manage.py makemigrations shop
# second command:  python manage.py migrate shop
