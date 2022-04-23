from rest_framework import generics
from . import serializers
from . import models
from .permissions import *


# Create your views here.

class UsersView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrCreateOnly]
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrOwner]
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
