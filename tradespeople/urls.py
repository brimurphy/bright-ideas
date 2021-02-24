from django.urls import path
from . import views

urlpatterns = [
    path('', views.trades_people, name='tradespeople'),
    path('<int:item_id>/', views.booking_form, name='booking_form'),
]
