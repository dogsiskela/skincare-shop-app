from django.shortcuts import render, redirect

from product.models import Product,ProductTag

def home_page(request):
    "Home page"
        
    if not request.user.is_authenticated:
         return redirect('/login')
    template_name = 'home.html'
    qs = Product.objects.all()[:3] 
    context = {'products': qs}
    return render(request, template_name, context)

def catalog_page(request):
    "Catalog page"
    
    if not request.user.is_authenticated:
        return redirect('/login')
    
    template_name = 'catalog.html'
    qs = Product.objects.all()
    context = {'products': qs}
    return render(request, template_name, context)

def product_preview(request,id):
    "Product preview page"
    
    if not request.user.is_authenticated:
        return redirect('/login')
     
    template_name = 'product.html'
    qs = Product.objects.get(pk=id)
    context = {'product':qs}
    return render(request,template_name,context)


def add_product(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("cost")
        category = request.POST.get("tag_id")
        in_stock = request.POST.get("in_stock")
        
        product = Product(name=name,description=description,price=price,in_stock=in_stock)
        product.save()
        
        product.category.add(ProductTag.objects.get(pk=category))
        return redirect('/catalog')
     
    tags = ProductTag.objects.all()
    context = {'tags':tags}
    template_name = 'add-product.html'
    return render(request,template_name,context)