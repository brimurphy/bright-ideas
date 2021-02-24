from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import TradesPeople
from .forms import BookingForm
from profiles.models import UserProfile


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
def booking_form(request, person_id):
    # A view to book a tradesperson
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Booking request has been sent to\
                {trades_booking.name}')
            return redirect(reverse('tradespeople'))

    form = BookingForm()
    trades_booking = get_object_or_404(TradesPeople, pk=person_id)

    template = 'tradespeople/booking_form.html'
    context = {
        'trades_booking': trades_booking,
        'form': form,
    }

    return render(request, template, context)
