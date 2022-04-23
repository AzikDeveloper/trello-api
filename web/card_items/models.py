from django.db import models
from card.models import Card
from board.models import Board


class Attachment(models.Model):
    card = models.ForeignKey(Card, related_name='attachments', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    file = models.FileField(upload_to='files/attachments', null=True)

    def __str__(self):
        return self.title


class Cover(models.Model):
    card = models.OneToOneField(Card, on_delete=models.CASCADE, null=True)

    class Color(models.Choices):
        GREEN = 'green'
        BLUE = 'blue'
        WHITE = 'white'
        RED = 'red'

    color = models.CharField(max_length=16, choices=Color.choices, default=Color.WHITE, blank=True, null=True)
    photo = models.ImageField(upload_to='images/covers', null=True)

    def __str__(self):
        return f'{self.color} cover of {self.card.title}'


class Checklist(models.Model):
    card = models.ForeignKey(Card, related_name='checklists', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=32, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Label(models.Model):
    board = models.ForeignKey(Board, related_name='labels', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=64, null=True)

    class Color(models.Choices):
        GREEN = 'green'
        BLUE = 'blue'
        WHITE = 'white'
        RED = 'red'

    color = models.CharField(max_length=16, choices=Color.choices, default=Color.GREEN, blank=True, null=True)

    def __str__(self):
        return self.name
