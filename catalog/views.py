from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    ind = Product.objects.all()
    context = {"ind": ind}
    return render(request, "products_list.html", context)


def catalog(request):
    return render(request, "catalog.html")


def mak(request, pk):
    prod = get_object_or_404(Product, id=pk)
    context = {"name": prod.name,
               "description": prod.description, }
    return render(request, "mak.html", context=context)
