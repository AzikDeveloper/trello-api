from rest_framework.permissions import BasePermission
from workspace.models import Workspace


class CanCreateBoard(BasePermission):
    def has_permission(self, request, view):
        workspace = Workspace.objects.filter(id=request.data.get('workspace_id')).filter(owner=request.user).exists()
        return workspace
