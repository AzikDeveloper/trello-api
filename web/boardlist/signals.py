from django.db.models.signals import post_save
from .models import Boardlist
from django.db.models import Max


def order_boardlist_on_create(sender, instance: Boardlist, created, **kwargs):
    if created:
        last_order = Boardlist.objects.aggregate(Max('order'))['order__max']
        instance.order = last_order + 1 if last_order else 1
        instance.save()


post_save.connect(order_boardlist_on_create, Boardlist)
