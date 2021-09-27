from django.db.models.fields import DateField
from django.shortcuts import render
from django.http import HttpResponse
from . models import LostItem
from datetime import datetime

# Create your views here.

def index(request):

    all_lost = LostItem.objects.all().order_by("datelost")

    lost_phones = all_lost.filter(typeofitem__contains = "phone")

    lost_today = all_lost.filter(datelost = datetime.now())

    context = {"all_lost" : all_lost, "lost_phones": lost_phones, "lost_today":lost_today}

    return render(request, 'lostandfound/index.html',context)