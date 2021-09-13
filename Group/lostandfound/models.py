from django.db import models

# Create your models here.

class LostItem(models.Model):
    typeofitem = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    datelost = models.DateField()
    contactinfo = models.CharField(max_length=2000)
    name = models.TextField(max_length=50)


class FoundItem(models.Model):
    pass

class Person(models.Model):
    pass
