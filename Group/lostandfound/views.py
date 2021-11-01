from django.db.models.fields import DateField
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . models import LostItem
from . models import FoundItem
from datetime import datetime

# Create your views here.

def index(request):

    all_lost = LostItem.objects.all().order_by("datelost")
    all_found = FoundItem.objects.all().order_by("datefound")

    lost_phones = all_lost.filter(typeofitem__contains = "phone")

    lost_today = all_lost.filter(datelost = datetime.now())
    found_today = all_lost.filter(datefound = datetime.now())

    context = {"all_lost" : all_lost, "lost_phones": lost_phones, "lost_today":lost_today, "all_found" : all_found, "found_today" : found_today}

    return render(request, 'lostandfound/index.html',context)

def detail(request,lost_id):

    item =get_object_or_404(LostItem, pk=lost_id)

    context = {"item": item}

    return render(request, 'lostandfound/detail.html', context)

def search(request):

    all_lost = LostItem.objects.all().order_by("datelost")
    
    if len(request.GET) == 0:
        relevant_lost = all_lost 
    else:
        search_string = request.GET['q']
        relevant_lost = all_lost.filter(typeofitem__contains = search_string)

    context = {'relevant_lost':relevant_lost}

    return render(request,'lostandfound/search.html', context)


