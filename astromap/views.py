from django.http import HttpResponse
from django.shortcuts import render

def ping(request):
    return HttpResponse("Hello, world!") # type:ignore

def index_view(request): 
    return render(request, "astromap/index.html")

def group0_view(request):
    return render(request, "astromap/group0.html")

def group1_view(request):
    return render(request, "astromap/group1.html")

def group2_view(request):
    return render(request, "astromap/group2.html")

def group3_view(request):
    return render(request, "astromap/group3.html")

def group4_view(request):
    return render(request, "astromap/group4.html")

def group5_view(request):
    return render(request, "astromap/group5.html")

