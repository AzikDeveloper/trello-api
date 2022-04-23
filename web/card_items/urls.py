from django.urls import path
from . import views

urlpatterns = [
    path('attachments/', views.CreateAttachmentView.as_view(), name='create-attachment'),
    path('attachments/<int:id>', views.AttachmentDetailView.as_view(), name='attachment-detail'),
    path('covers/', views.CreateAttachmentView.as_view(), name='create-attachment'),
    path('covers/<int:id>', views.AttachmentDetailView.as_view(), name='attachment-detail'),
    path('checklists/', views.CreateAttachmentView.as_view(), name='create-attachment'),
    path('checklists/<int:id>', views.AttachmentDetailView.as_view(), name='attachment-detail'),
    path('labels/', views.CreateAttachmentView.as_view(), name='create-attachment'),
    path('labels/<int:id>', views.AttachmentDetailView.as_view(), name='attachment-detail')
]
