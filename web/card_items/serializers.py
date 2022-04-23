from .models import *
from rest_framework import serializers


class AttachmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'title', 'file']


class CoverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ['id', 'color', 'photo']


class ChecklistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = ['id', 'title', 'done']


class LabelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name', 'color']


class CreateAttachmentSerializer(serializers.ModelSerializer):
    card_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Attachment
        fields = ['id', 'card_id', 'title', 'file']


class CreateCoverSerializer(serializers.ModelSerializer):
    card_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Cover
        fields = ['id', 'card_id', 'color', 'photo']


class CreateChecklistSerializer(serializers.ModelSerializer):
    card_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Checklist
        fields = ['id', 'card_id', 'title', 'done']


class CreateLabelSerializer(serializers.ModelSerializer):
    card_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Label
        fields = ['id', 'card_id', 'name', 'color']
