from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateBoardlistView.as_view(), name='create-boardlist'),
    path('<int:id>', views.BoardlistDetailView.as_view(), name='boardlist-detail')
]
