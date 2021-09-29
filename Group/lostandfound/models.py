from django.db import models

# Create your models here.

class LostItem(models.Model):
    
    typeofitem = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    datelost = models.DateField()
    contactinfo = models.CharField(max_length=2000)
    name = models.CharField(max_length=50)
    #itemid = models.IntegerField() don't know how to use this yet


class FoundItem(models.Model):
    pass

class User(models.Model):
    pass
