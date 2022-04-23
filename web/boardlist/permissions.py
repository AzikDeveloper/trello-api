from rest_framework.permissions import BasePermission
from rest_framework.generics import get_object_or_404
from board.models import Board
from django.db.models import Q
from boardlist.models import Boardlist


class CanCreateBoardlist(BasePermission):
    def has_permission(self, request, view):
        board = get_object_or_404(Board, id=request.data.get('board_id'))
        conditions = (
            board.members.filter(id=request.user.id).exists(),
            board.workspace.members.filter(id=request.user.id),
            board.workspace.owner == request.user
        )
        return any(conditions)


class CanManipulateBoardlist(BasePermission):
    def has_object_permission(self, request, view, boardlist):
        return Boardlist.objects.filter(id=boardlist.id).filter(
            Q(board__members=request.user) |
            Q(board__guests=request.user) |
            Q(board__workspace__owner=request.user) |
            Q(board__workspace__members=request.user)).exists()
