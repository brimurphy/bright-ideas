from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages


from .models import Reviews
from .forms import ReviewForm


def reviews(request, trades_person_id):
    """ A view to return the review page """

    reviews = Reviews.objects.filter(trades_person=trades_person_id)
    total = sum(review.rating for review in reviews)
    avg = total // reviews.count()
    return JsonResponse({'avg': avg, 'reviews': list(reviews.values())},)
