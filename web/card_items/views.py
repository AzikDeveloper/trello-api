from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import CanCreateCardItem, CanManipulateCardItem
from rest_framework.parsers import MultiPartParser


class CreateAttachmentView(CreateAPIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, CanCreateCardItem]
    queryset = Attachment.objects.all()
    serializer_class = CreateAttachmentSerializer


class AttachmentDetailView(RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser]
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, CanManipulateCardItem]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentDetailSerializer


class CreateCoverView(CreateAPIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, CanCreateCardItem]
    queryset = Cover.objects.all()
    serializer_class = CreateCoverSerializer


class CoverDetailView(RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser]
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, CanManipulateCardItem]
    queryset = Cover.objects.all()
    serializer_class = CoverDetailSerializer


class CreateChecklistView(CreateAPIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, CanCreateCardItem]
    queryset = Checklist.objects.all()
    serializer_class = CreateChecklistSerializer


class ChecklistDetailView(RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser]
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, CanManipulateCardItem]
    queryset = Checklist.objects.all()
    serializer_class = ChecklistDetailSerializer


class CreateLabelView(CreateAPIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, CanCreateCardItem]
    queryset = Label.objects.all()
    serializer_class = CreateLabelSerializer


class LabelDetailView(RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser]
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, CanManipulateCardItem]
    queryset = Attachment.objects.all()
    serializer_class = LabelDetailSerializer
