from django.db import models
from boardlist.models import Boardlist


class Card(models.Model):
    boardlist = models.ForeignKey(Boardlist, related_name='cards', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=64, null=True)
    description = models.TextField(null=True, blank=True)
    labels = models.ManyToManyField('card_items.Label', related_name='labels', blank=True)
    members = models.ManyToManyField('users.User', related_name='cards_as_member', blank=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
