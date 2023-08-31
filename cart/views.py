from django.shortcuts import render,redirect
from cart.models import Cart,CartItem
from product.models import Product


def cart(request):
    
    if not request.user.is_authenticated:
        return redirect('/login')
     
    template_name = 'cart.html'
    context = {}
    cart_exists = Cart.objects.get(user__pk=request.user.pk)
    
    if request.method == 'POST':
        user_cart_exists = Cart.objects.filter(user__pk=request.user.pk).exists()
        if(user_cart_exists):
            print("exists")
            cart = Cart.objects.get(user__pk=request.user.pk)
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                product = Product.objects.get(pk=item.product.pk)
                product.in_stock = product.in_stock-item.quantity
                product.save()
            cart_items.delete()
    
    if(cart_exists):
        cart_items = CartItem.objects.filter(cart__user__pk=request.user.pk)
        context['cart_items']=cart_items
    return render(request,template_name,context)

def cart_add(request,id):
    if not request.user.is_authenticated:
        return redirect('/login')
    print(request.user.pk)
    user_cart_exists = Cart.objects.filter(user__pk=request.user.pk).exists()
    if(not user_cart_exists):
        cart = Cart(user=request.user)
        cart.save()   
        
    cart = Cart.objects.get(user__pk=request.user.pk)
    cart_item_exists = CartItem.objects.filter(cart=cart,product__pk = id).exists()
    if(cart_item_exists):
        cart_item = CartItem.objects.get(cart=cart,product__pk = id)
        cart_item.quantity=cart_item.quantity+1
        cart_item.save()
    else:
        cart_item = CartItem(cart=cart,quantity=1,product=Product.objects.get(pk=id))
        cart_item.save()
      
    return redirect('/cart')
