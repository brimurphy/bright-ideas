from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Reviews
from .forms import ReviewForm


def reviews(request, trades_person_id):
    """ A view to return the review page """

    reviews = Reviews.objects.filter(trades_person=trades_person_id)
    total = sum(review.rating for review in reviews)
    avg = total // reviews.count()
    return JsonResponse({'avg': avg, 'reviews': list(reviews.values())},)


@login_required
def add_reviews(request):
    # Allow users to post reviews on tradespeople
    reviews = Reviews.objects.all().values()

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'New review added!')
            return redirect(reverse('tradespeople',))
        else:
            messages.error(request, 'Failed to add review!')
    else:

        template = 'reviews/add_reviews.html'
        context = {
            'reviews': reviews,
        }

        return render(request, template, context)

@login_required
def add_trades_person_review(request, trades_person_id):
    # Allow users to post reviews on tradespeople
    reviews = Reviews.objects.select_related('user').select_related('trades_person').all()
    print(Reviews.objects.select_related('user').select_related('trades_person').all().query)
    form = ReviewForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save()
            messages.success(request, 'New review added!')
            return redirect(reverse('tradespeople',))
        else:
            messages.error(request, 'Failed to add review!')
    else:

        template = 'reviews/add_reviews.html'
        context = {
            'reviews': reviews,
            'trades_person_id': trades_person_id,
            'form': form,
        }

        return render(request, template, context)
