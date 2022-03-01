from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.sponsor_levels import SponsorLevel
from conferences.serializers.sponsor_levels import SponsorLevelSerializer


class SponsorLevelViewSet(viewsets.ModelViewSet):
    queryset = SponsorLevel.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = SponsorLevelSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
