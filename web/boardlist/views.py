from .serializers import CreateBoardlistSerializer, BoardlistDetailSerializer
from rest_framework import generics
from .permissions import CanCreateBoardlist, CanManipulateBoardlist
from .models import Boardlist
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.parsers import MultiPartParser


class CreateBoardlistView(generics.CreateAPIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, CanCreateBoardlist]
    queryset = Boardlist.objects.all()
    serializer_class = CreateBoardlistSerializer


class BoardlistDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, CanManipulateBoardlist]
    queryset = Boardlist.objects.all()
    serializer_class = BoardlistDetailSerializer
