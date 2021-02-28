from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_reviews, name='add_reviews'),
    path(
        'add/<int:trades_person_id>/',
        views.add_trades_person_review,
        name='add_trades_person_review'),
    path('<int:trades_person_id>/', views.reviews, name='reviews'),
]
