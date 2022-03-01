from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.sponsors import Sponsor
from conferences.serializers.sponsors import SponsorSerializer


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = SponsorSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
