from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    photo = models.FileField(upload_to='profile_pics', null=True, blank=True)
