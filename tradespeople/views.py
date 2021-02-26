from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


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


def booking_email(user_info, trades_person_name, date):
    cust_email = user_info.default_email

    subject = render_to_string(
        'confirmation_emails/confirmation_booking_email_subject.txt',
        {'trades_person': trades_person_name})
    body = render_to_string(
            'confirmation_emails/confirmation_booking_email_body.txt',
            {'user_name': user_info.default_full_name,
             'contact_email': settings.DEFAULT_FROM_EMAIL,
             'date': date,
             'trades_person': trades_person_name})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


@login_required
def booking_form(request, person_id):
    # A view to book a tradesperson
    user_info = get_object_or_404(UserProfile, user=request.user)
    trades_person = get_object_or_404(TradesPeople, pk=person_id)

    if request.method == 'POST':
        date = request.POST.get('date')
        form = BookingForm(request.POST, instance=user_info)
        if form.is_valid():
            messages.success(request, 'Booking Complete')
            booking_email(user_info, trades_person.name, date)
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Booking Failed!!')
    else:
        form = BookingForm(instance=user_info)

    template = 'tradespeople/booking_form.html'
    context = {
        'trades_person': trades_person,
        'form': form,
    }

    return render(request, template, context)
