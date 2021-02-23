from django.shortcuts import render
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
