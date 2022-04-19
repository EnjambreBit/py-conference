from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.event_registrations import EventRegistration
from conferences.serializers.event_registrations import EventRegistrationSerializer


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EventRegistrationSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
