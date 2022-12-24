from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hii(request):
    return HttpResponse('<i>hii welcome to my project</i>')

def hello(request):
    return HttpResponse('<i>HELLO WELCOME TO MY PROJECT</i>')