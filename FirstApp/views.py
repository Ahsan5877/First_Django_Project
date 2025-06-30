from django.shortcuts import render
from django.http import HttpResponse

def FirstApp(request):
    return HttpResponse("Hello world!")

