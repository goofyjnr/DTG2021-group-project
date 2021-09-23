from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #code here

    return HttpResponse('you made it to index')