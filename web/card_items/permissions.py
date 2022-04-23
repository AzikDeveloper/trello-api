from rest_framework.permissions import BasePermission
from rest_framework.generics import get_object_or_404
from card.models import Card


class CanCreateCardItem(BasePermission):
    def has_permission(self, request, view):
        card = get_object_or_404(Card, id=request.data.get('card_id'))
        conditions = (
            card.boardlist.board.members.filter(id=request.user.id).exists(),
            card.boardlist.board.workspace.owner == request.user,
            card.boardlist.board.workspace.members.filter(id=request.user.id)
        )
        return any(conditions)


class CanManipulateCardItem(BasePermission):
    def has_object_permission(self, request, view, item):
        conditions = (
            item.card.boardlist.board.members.filter(id=request.user.id),
            item.card.boardlist.board.workspace.owner == request.user,
            item.card.boardlist.board.workspace.members.filter(id=request.user.id)
        )
        return any(conditions)
