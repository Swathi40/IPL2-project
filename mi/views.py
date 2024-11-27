from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def captain(request):
    return HttpResponse('<h1>Any one is not here</h1>') 

def vicecaptain(request):
    return HttpResponse('<i>None of them</i>')
