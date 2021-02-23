from django.urls import path
from . import views

urlpatterns = [
    path('', views.trades_people, name='tradespeople'),
]
