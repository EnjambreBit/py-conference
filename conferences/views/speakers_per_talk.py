from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.speakers_per_talk import SpeakerPerTalk
from conferences.serializers.speakers_per_talk import SpeakerPerTalkSerializer


class SpeakerPerTalkViewSet(viewsets.ModelViewSet):
    queryset = SpeakerPerTalk.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = SpeakerPerTalkSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
