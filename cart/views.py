from django.shortcuts import render, redirect
from django.contrib import messages
from gadget.models import Product


def view_cart(request):
    return render(request, "cart/view_cart.html")


def add_cart(request, product_id):
    product = Product.objects.get(asin=product_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
        messages.success(request, f'Your item {product.title} has been added to the cart.')
    request.session["cart"] = cart
    print(request.session["cart"])
    return redirect(redirect_url)

def edit_cart(request, product_id):
    """ Adjust the quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, asin=product_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:

        cart[item_id] = quantity
        messages.success(request, f'Updated {product.title} quantity to the {cart[product_id]}')

    else:
        cart.pop(product_id)
        messages.success(request, f'Removed {product.title} from your shopping cart')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def subtract_from_cart(request, product_id):
    """Remove item from the shopping bag """
    product = get_object_or_404(Product, asin=product_id)

    try:
        cart = request.session.get('cart', {})
        cart.pop(product_id)
        messages.success(request, f'Removed {product.title} from your shopping cart')


        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
