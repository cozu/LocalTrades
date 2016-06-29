from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    photo = models.CharField(max_length=100)
    price = models.FloatField()
    user = models.ForeignKey(User, unique=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
