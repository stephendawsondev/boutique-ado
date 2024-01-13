from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, create, **kwargs):
    """
    Update order total on lineitem update/create
    """
    print('sender', sender)
    print('instance', instance)
    print('create', create)
    print('kwargs', kwargs)
    print('running update_on_save')
    instance.order.update_total()


@receiver(post_save, sender=OrderLineItem)
def delete_on_save(sender, instance, **kwargs):
    """
    Delete order total on lineitem update/create
    """
    print('sender', sender)
    print('instance', instance)
    print('kwargs', kwargs)
    print('running delete_on_save')
    instance.order.update_total()
