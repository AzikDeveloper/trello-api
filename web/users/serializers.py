from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'photo', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'allow_null': False,
                'required': True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance: User, validated_data):
        instance.set_password(validated_data.pop('password'))
        for field, value in validated_data.items():
            if hasattr(instance, field):
                setattr(instance, field, value)
            else:
                raise ValidationError({field: 'this is field is not exist'})
        instance.save()
        return instance

    def validate_password(self, password):
        validate_password(password)
        return password
