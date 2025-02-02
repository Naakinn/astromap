from django.http import HttpResponse
from django.shortcuts import render

def ping(request):
    return HttpResponse("Hello, world!") # type:ignore

def index_view(request): 
    return render(request, "astromap/index.html")
