from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total when line item updates or is created
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def delete_on_save(sender, instance, **kwargs):
    """
    Update order total when line item deleted
    """
    instance.order.update_total()
