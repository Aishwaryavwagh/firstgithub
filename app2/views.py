from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def geetha(request):
    return HttpResponse('<h1>My SuperMan</h1>')

def dubbii(request):
    return HttpResponse('<h1>My Strength</h1>')