from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def captain(request):
    return HttpResponse('<h1>king kohili is captain of rcb</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>none of them</h1>')