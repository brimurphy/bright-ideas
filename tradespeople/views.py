from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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


def booking_email(userInfo):
    cust_email = userInfo.default_email

    send_mail(
        'Test Email',
        'This is a test for booking',
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


@login_required
def booking_form(request, person_id):
    # A view to book a tradesperson
    user_Info = get_object_or_404(UserProfile, user=request.user)
    trades_booking = get_object_or_404(TradesPeople, pk=person_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=user_Info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking Complete')
            booking_email(user_Info)
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Booking Failed!!')
    else:
        form = BookingForm(instance=user_Info)

    template = 'tradespeople/booking_form.html'
    context = {
        'trades_booking': trades_booking,
        'form': form,
        'user_Info': user_Info,
    }

    return render(request, template, context)
