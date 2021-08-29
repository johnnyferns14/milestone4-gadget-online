from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from gadget.models import Product


def cartItems(request):
    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, asin=product_id)
        total += quantity * product.price
        item_count += quantity
        cart_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.MINIMUM_PURCHASE_LIMIT:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_RATE / 100)
        free_delivery_target = settings.FREE_DELIVERY_LIMIT - total
    else:
        delivery = 0
        free_delivery_target = 0

    grand_total = delivery + total

    context = {
        "cart_items": cart_items,
        "total": total,
        "item_count": item_count,
        "delivery": delivery,
        "free_delivery_target": free_delivery_target,
        "free_delivery_limit": settings.FREE_DELIVERY_LIMIT,
        "grand_total": grand_total
    }

    return context
