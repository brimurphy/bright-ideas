from django.db import models

from profiles.models import UserProfile
from tradespeople.models import TradesPeople


class Reviews(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='')
    trades_person = models.ForeignKey(
        TradesPeople, on_delete=models.CASCADE, null=False, blank=False)
    comment = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
