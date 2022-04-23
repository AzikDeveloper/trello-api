from rest_framework.permissions import BasePermission
from rest_framework.generics import get_object_or_404
from boardlist.models import Boardlist


class CanCreateCard(BasePermission):
    def has_permission(self, request, view):
        boardlist = get_object_or_404(Boardlist, id=request.data.get('boardlist_id'))
        return boardlist.board.members.filter(
            id=request.user.id).exists() or boardlist.board.workspace.owner == request.user


class CanManipulateCard(BasePermission):
    def has_object_permission(self, request, view, card):
        conditions = (
            card.boardlist.board.members.filter(id=request.user.id),
            card.boardlist.board.workspace.owner == request.user,
            card.boardlist.board.workspace.members.filter(id=request.user.id)
        )
        return any(conditions)
