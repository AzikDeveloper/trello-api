from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateCardView.as_view(), name='create-card'),
    path('<int:id>', views.CardDetailView.as_view(), name='card-detail'),
    path('<int:c_id>/members', views.CardMembersListCreateView.as_view(), name='card-members'),
    path('<int:c_id>/members/<int:u_id>', views.RemoveMemberFromCardView.as_view(), name='remove-member-from-card')
]
