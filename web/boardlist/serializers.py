from rest_framework import serializers
from .models import Boardlist
from card.serializers import CardDetailSerializer


class CreateBoardlistSerializer(serializers.ModelSerializer):
    board_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Boardlist
        fields = ['id', 'board_id', 'title']


class BoardlistDetailSerializer(serializers.ModelSerializer):
    cards = CardDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Boardlist
        fields = ['id', 'order', 'title', 'cards']
