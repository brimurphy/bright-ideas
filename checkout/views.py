from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IACGMExrtPNf4ef5wZlW4ANk493wp2waAgRjpi1mTPx8Pg648hcIFMsulpJsw7AAZZloPMKPNQ3wQvhZHnSIj2700zjPxKeVl',
        'client_secret': 'test client_secret',
    }

    return render(request, template, context)
