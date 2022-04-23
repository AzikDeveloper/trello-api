from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateBoardView.as_view(), name='create-board'),
    path('<int:id>', views.BoardDetailView.as_view(), name='manipulate-board'),
    path('<int:id>/boardlists', views.BoardListsOfBoardView.as_view(), name='boardlists'),
    path('<int:id>/labels', views.LabelsOfBoardView.as_view(), name='labels'),
    path('<int:b_id>/members', views.BoardMembersListCreateView.as_view(), name='board-members'),
    path('<int:b_id>/members/<int:u_id>', views.RemoveMemberFromBoardView.as_view(), name='remover-member-from-board'),
    path('<int:b_id>/guests', views.BoardGuestsListCreateView.as_view(), name='board-guests'),
    path('<int:b_id>/guests/<int:u_id>', views.RemoveGuestFromBoardView.as_view(), name='remover-guest-from-board')
]
