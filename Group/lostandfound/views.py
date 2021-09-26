from django.shortcuts import render
from django.http import HttpResponse
from . models import LostItem

# Create your views here.

def index(request):

    all_lost = LostItem.objects.all()

    context = {"all_lost" : all_lost}

    return render(request, 'lostandfound/index.html',context)