from card_items.serializers import *
from users.serializers import UserSerializer


class CreateCardSerializer(serializers.ModelSerializer):
    boardlist_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Card
        fields = ['id', 'boardlist', 'boardlist_id', 'title', 'description', 'start_date', 'due_date', 'done']


class CardDetailSerializer(serializers.ModelSerializer):
    labels = LabelDetailSerializer(many=True, read_only=True)
    members = UserSerializer(many=True, read_only=True)
    attachments = AttachmentDetailSerializer(many=True, read_only=True)
    checklists = ChecklistDetailSerializer(many=True, read_only=True)
    cover = CoverDetailSerializer(read_only=True)

    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'labels', 'members', 'attachments', 'checklists', 'cover',
                  'start_date', 'due_date', 'done']
