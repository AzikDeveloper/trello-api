from django.db import models
from workspace.models import Workspace
from users.models import User


class Board(models.Model):
    class Visibility(models.Choices):
        PUBLIC = 'public'
        PRIVATE = 'private'
        BLOCKED = 'blocked'

    workspace = models.ForeignKey(Workspace, related_name='boards', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=64, null=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/boards', null=True, blank=True)
    members = models.ManyToManyField(User, related_name='boards_as_member', blank=True)
    guests = models.ManyToManyField(User, related_name='boards_as_guest', blank=True)
    visibility = models.CharField(max_length=64, choices=Visibility.choices, null=True, default=Visibility.PRIVATE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'
