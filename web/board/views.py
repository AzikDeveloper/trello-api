from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Board
from . import serializers
from rest_framework.generics import get_object_or_404
from boardlist.models import Boardlist
from rest_framework.exceptions import PermissionDenied
from .permissions import CanCreateBoard
from boardlist.serializers import BoardlistDetailSerializer
from card_items.models import Label
from card_items.serializers import LabelDetailSerializer
from rest_framework.views import APIView
from users.models import User
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from django.db.models import Q


class CreateBoardView(generics.CreateAPIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, CanCreateBoard]
    queryset = Board.objects.all()
    serializer_class = serializers.CreateBoardSerializer


class BaseBoardMixin:
    def get_board(self):
        if self.request.method == 'GET':
            board = Board.objects.filter(id=self.kwargs.get(self.lookup_field)).filter(
                Q(members__in=[self.request.user]) |
                Q(guests__in=[self.request.user]) |
                Q(workspace__members__in=[self.request.user]) |
                Q(workspace__owner=self.request.user)
            ).first()
        else:
            board = Board.objects.filter(id=self.kwargs.get(self.lookup_field)).filter(
                workspace__owner=self.request.user).first()
        if board:
            return board
        else:
            raise PermissionDenied()


class BoardDetailView(BaseBoardMixin, generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = Board.objects.all()
    serializer_class = serializers.BoardDetailSerializer

    def get_object(self):
        return self.get_board()


class BoardListsOfBoardView(BaseBoardMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = Boardlist.objects.all()
    serializer_class = BoardlistDetailSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(board=self.get_board())


class LabelsOfBoardView(BaseBoardMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = Label.objects.all()
    serializer_class = LabelDetailSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(board=self.get_board())


class BoardMembersListCreateView(BaseBoardMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'b_id'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(boards_as_member__in=[self.get_board()])

    def post(self, request, *args, **kwargs):
        board = self.get_board()
        member = get_object_or_404(User, id=self.request.data.get('user_id'))
        board.members.add(member)
        return Response(status=status.HTTP_200_OK)


class RemoveMemberFromBoardView(BaseBoardMixin, APIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'b_id'

    def delete(self, request, *args, **kwargs):
        board = self.get_board()
        member = get_object_or_404(User, id=self.kwargs.get('u_id'))
        board.members.remove(member)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BoardGuestsListCreateView(BaseBoardMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'b_id'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(boards_as_guest__in=[self.get_board()])

    def post(self, request, *args, **kwargs):
        board = self.get_board()
        guest = get_object_or_404(User, id=self.request.data.get('user_id'))
        board.guests.add(guest)
        return Response(status=status.HTTP_200_OK)


class RemoveGuestFromBoardView(BaseBoardMixin, APIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'b_id'

    def delete(self, request, *args, **kwargs):
        board = self.get_board()
        guest = get_object_or_404(User, id=self.kwargs.get('u_id'))
        board.guests.remove(guest)
        return Response(status=status.HTTP_204_NO_CONTENT)
