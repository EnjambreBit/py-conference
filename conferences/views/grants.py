from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.grants import Grant
from conferences.serializers.grants import GrantSerializer


class GrantViewSet(viewsets.ModelViewSet):
    queryset = Grant.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = GrantSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
