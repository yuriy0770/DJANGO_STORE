from django.shortcuts import render

def home(request):
    return render(request, "catalog/home.html")

def catalog(request):
    return render(request, "catalog/catalog.html")