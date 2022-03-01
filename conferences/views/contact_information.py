from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.contact_information import ContactInformation
from conferences.serializers.contact_information import ContactInformationSerializer


class ContactInformationViewSet(viewsets.ModelViewSet):
    queryset = ContactInformation.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ContactInformationSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
