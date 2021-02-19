from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


# Create your views here.
def view_cart(request):
    """ A view to return items in your shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of an item to the cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'{cart[item_id]} {product.name} added to your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'{product.name} added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Update the quantity of an item in the cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request,
            f'There is now {cart[item_id]} {product.name} in your cart')
    else:
        cart.pop(item_id)
        messages.success(request, f'{product.name} removed from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_item_cart(request, item_id):
    """ Remove an item from the cart """
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})

    try:
        cart.pop(item_id)
        messages.success(request, f'{product.name} removed from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request, f'Something went wrong!\
             We couldn\'t remove {e} from your cart')
        return HttpResponse(status=500)
