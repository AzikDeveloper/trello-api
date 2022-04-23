from rest_framework import serializers
from .models import Workspace


class WorkspaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['id', 'name', 'photo']


class WorkspaceDetailSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'description', 'photo', 'visibility', 'owner', 'owner_id']
