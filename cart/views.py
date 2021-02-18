from django.shortcuts import render


# Create your views here.
def view_cart(request):
    """ A view to return items in your shopping cart """
    
    return render(request, 'cart/cart.html')
