from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *
from .models import Workspace
from users.serializers import UserSerializer
from users.models import User
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from board.models import Board
from card_items.models import *
from board.serializers import BoardsListSerializer
from rest_framework.parsers import MultiPartParser, JSONParser
from django.db.models import Q
from django.db.utils import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response


class MyWorkspacesListCreateView(ListCreateAPIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    queryset = Workspace.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.WorkspaceListSerializer
        else:
            return serializers.WorkspaceDetailSerializer

    def filter_queryset(self, queryset):
        queryset = queryset.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user.id)


class BaseWorkspaceMixin:
    def get_workspace(self):
        if self.request.method == 'GET':
            workspace = Workspace.objects.filter(id=self.kwargs.get('w_id')).filter(
                Q(members__in=[self.request.user]) | Q(owner=self.request.user)).first()
        else:
            workspace = Workspace.objects.filter(id=self.kwargs.get('w_id')).filter(owner=self.request.user).first()
        if workspace:
            return workspace
        else:
            raise PermissionDenied()


class WorkspaceDetailView(RetrieveUpdateDestroyAPIView, BaseWorkspaceMixin):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    queryset = Workspace.objects.all()
    serializer_class = serializers.WorkspaceDetailSerializer

    def get_object(self):
        return self.get_workspace()


class WorkspaceMembersListCreateView(ListAPIView, BaseWorkspaceMixin):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(workspaces_as_member__in=[self.get_workspace()])

    def post(self, request, *args, **kwargs):
        workspace = self.get_workspace()
        try:
            workspace.members.add(request.data.get('user_id'))
        except IntegrityError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_201_CREATED)


class RemoveMemberFromWorkspaceView(APIView, BaseWorkspaceMixin):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        workspace = self.get_workspace()
        workspace.members.remove(self.kwargs.get('u_id'))
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkspaceBoardsListView(ListAPIView, BaseWorkspaceMixin):
    permission_classes = [IsAuthenticated]
    queryset = Board.objects.all()
    serializer_class = BoardsListSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(workspace=self.get_workspace())


@api_view(["GET"])
def load_test(request, query_count):
    datas = []
    for i in range(query_count):
        datas.append(serializers.WorkspaceListSerializer(Workspace.objects.all(), many=True).data)

    return Response(data=datas)
