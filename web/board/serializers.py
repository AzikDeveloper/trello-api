from rest_framework import serializers
from .models import Board
from boardlist.serializers import *


class BoardsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name', 'photo']


class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name', 'description', 'photo']


class CreateBoardSerializer(serializers.ModelSerializer):
    workspace_id = serializers.IntegerField()

    class Meta:
        model = Board
        fields = ['id', 'workspace_id', 'name', 'description', 'photo']
