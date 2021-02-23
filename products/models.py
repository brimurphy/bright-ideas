from django.db import models


# Category Model
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Product Model
class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        upload_to='products/', null=True, blank=True)
    ip_rating = models.CharField(max_length=4, null=True, blank=True)
    bulb_type = models.CharField(max_length=20, null=True, blank=True)
    is_dimmable = models.BooleanField(default=False)
    is_clearance = models.BooleanField(default=False)
    is_multipack = models.BooleanField(default=False)

    def __str__(self):
        return self.name
