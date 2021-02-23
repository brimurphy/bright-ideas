from django.db import models


class TradesPeople(models.Model):
    # Recommended Trade workers
    class Meta:
        verbose_name_plural = 'Trades People'

    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
