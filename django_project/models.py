from django.db import models


class Stuff(models.Model):
    name = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=10)
    cost = models.IntegerField(max_length=10)
    weight = models.IntegerField(max_length=10)
    image = models.CharField(max_length=30)
