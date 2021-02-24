from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import TradesPeople


@login_required
def trades_people(request):
    # View for registered users to view recommende trades people
    trades_people = TradesPeople.objects.all()

    template = 'tradespeople/tradespeople.html'
    context = {
        'trades_people': trades_people,
    }

    return render(request, template, context)


@login_required
def booking_form(request, item_id):
    # A view to book a tradesperson
    trades_booking = get_object_or_404(TradesPeople, pk=item_id)

    template = 'tradespeople/booking_form.html'
    context = {
        'trades_booking': trades_booking,
    }

    return render(request, template, context)
