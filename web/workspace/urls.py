from django.urls import path
from . import views

urlpatterns = [
    path('mine', views.MyWorkspacesListCreateView.as_view(), name='workspaces'),
    path('<int:w_id>', views.WorkspaceDetailView.as_view(), name='workspace-detail'),
    path('<int:w_id>/members', views.WorkspaceMembersListCreateView.as_view(), name='workspace-members'),
    path('<int:w_id>/members/<int:u_id>', views.RemoveMemberFromWorkspaceView.as_view(),
         name='remove-member-from-workspace'),
    path('<int:w_id>/boards', views.WorkspaceBoardsListView.as_view(), name='workspace-boards')
]
