from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.event_links import EventLink
from conferences.serializers.event_links import EventLinkSerializer


class EventLinkViewSet(viewsets.ModelViewSet):
    queryset = EventLink.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EventLinkSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
