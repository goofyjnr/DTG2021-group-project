from django.db import models

# Create your models here.

class LostItem(models.Model):
    
    title = models.CharField(max_length=50)
    typeofitem = models.CharField(max_length=200)
    description = models.TextField()
    datelost = models.DateField()
    contactinfo = models.CharField(max_length=2000)
    name = models.CharField(max_length=50)
    #itemid = models.IntegerField() don't know how to use this yet


class FoundItem(models.Model):
    title =  models.CharField(max_length=50)
    typeofitem = models.CharField(max_length=200)
    description = models.TextField()
    datefound = models.DateField()
    contactinfo = models.CharField(max_length=2000)
    name = models.CharField(max_length=50)

#class User(models.Model):
 #   pass
