from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is your first Django app!")
# Create your views here.
