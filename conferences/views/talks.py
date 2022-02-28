from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.talks import Talk
from conferences.serializers.talks import TalkSerializer


class TalkViewSet(viewsets.ModelViewSet):
    queryset = Talk.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TalkSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
