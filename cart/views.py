from django.shortcuts import render, redirect
from django.contrib import messages
from gadget.models import Product


def viewCart(request):
    return render(request, "cart/view_cart.html")


def addToCart(request, product_id):
    product = Product.objects.get(asin=product_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
        messages.success(request, f'Your item {product.name} has been added to the cart.')
    request.session["cart"] = cart
    print(request.session["cart"])
    return redirect(redirect_url)
