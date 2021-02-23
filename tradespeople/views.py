from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def trades_people(request):
    # View for registered users to view recommende trades people

    template = 'tradespeople/tradespeople.html'

    return render(request, template)
