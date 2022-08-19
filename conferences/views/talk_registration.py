from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.talk_registration import TalkRegistration
from conferences.serializers.talk_registration import TalkRegistrationSerializer


class TalkRegistrationViewSet(viewsets.ModelViewSet):
    queryset = TalkRegistration.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TalkRegistrationSerializer

