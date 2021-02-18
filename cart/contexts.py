from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    free_delivery = settings.FREE_DELIVERY_THRESHOLD
    delivery_cost = settings.STANDARD_DELIVERY_PERCENTAGE
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        cart_items.append({
           'item_id': item_id,
           'quantity': quantity,
           'product': product,
        })

    if total < free_delivery:
        delivery = total * Decimal(delivery_cost / 100)
        free_delivery_delta = free_delivery - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'free_delivery': free_delivery,
        'free_delivery_delta': free_delivery_delta,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
