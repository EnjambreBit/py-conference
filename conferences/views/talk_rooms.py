from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.talk_rooms import TalkRoom
from conferences.serializers.talk_rooms import TalkRoomSerializer


class TalkRoomViewSet(viewsets.ModelViewSet):
    queryset = TalkRoom.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TalkRoomSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
