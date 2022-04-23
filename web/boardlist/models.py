from django.db import models
from board.models import Board


class Boardlist(models.Model):
    board = models.ForeignKey(Board, related_name='boardlists', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=64, null=True)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Boardlist'
        verbose_name_plural = 'Boardlists'
