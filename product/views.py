from django.shortcuts import render

from product.models import Product

def home_page(request):
    "Home page"
    
    template_name = 'home.html'
    qs = Product.objects.all()[:3] 
    context = {'products': qs}
    return render(request, template_name, context)

def catalog_page(request):
    "Catalog page"
    
    template_name = 'catalog.html'
    qs = Product.objects.all()
    context = {'products': qs}
    return render(request, template_name, context)