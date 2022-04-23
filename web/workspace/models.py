from django.db import models
from users.models import User


class Workspace(models.Model):
    class Visibility(models.Choices):
        PUBLIC = 'public'
        PRIVATE = 'private'
        BLOCKED = 'blocked'

    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/workspaces', null=True, blank=True)
    visibility = models.CharField(max_length=64, choices=Visibility.choices, null=True, default=Visibility.PRIVATE)
    owner = models.ForeignKey(User, related_name='workspaces_as_owner', on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(User, related_name='workspaces_as_member', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Workspace'
        verbose_name_plural = 'Workspaces'
