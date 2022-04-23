from . import serializers
from .permissions import CanCreateCard, CanManipulateCard
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Card
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from users.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class CreateCardView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, CanCreateCard]
    queryset = Card.objects.all()
    serializer_class = serializers.CreateCardSerializer


class CardDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, CanManipulateCard]
    queryset = Card.objects.all()
    serializer_class = serializers.CardDetailSerializer


class BaseCardPermissionMixin:
    def get_card(self):
        card = get_object_or_404(Card, id=self.kwargs.get('c_id'))
        conditions = (
            card.boardlist.board.members.filter(id=self.request.user.id),
            card.boardlist.board.workspace.owner == self.request.user,
            card.boardlist.board.workspace.members.filter(id=self.request.user.id)
        )
        if any(conditions):
            return card
        else:
            raise PermissionDenied()


class CardMembersListCreateView(APIView, BaseCardPermissionMixin):
    permission_classes = [IsAuthenticated]

    def get_member(self):
        member = get_object_or_404(User, id=self.request.data.get('user_id'))
        return member

    def get(self, request, *args, **kwargs):
        card = self.get_card()
        members = card.members.all()
        return Response(data=UserSerializer(members, many=True).data)

    def post(self, request, *args, **kwargs):
        card = self.get_card()
        member = self.get_member()
        card.members.add(member)
        card.save()
        return Response(status=status.HTTP_200_OK)


class RemoveMemberFromCardView(APIView, BaseCardPermissionMixin):
    permission_classes = [IsAuthenticated]

    def get_member(self):
        member = get_object_or_404(User, id=self.kwargs.get('u_id'))
        return member

    def delete(self, request, *args, **kwargs):
        board = self.get_card()
        member = self.get_member()
        board.members.remove(member)
        board.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
