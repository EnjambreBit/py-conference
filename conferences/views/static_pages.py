from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.static_pages import StaticPage
from conferences.serializers.static_pages import StaticPageSerializer


class StaticPageViewSet(viewsets.ModelViewSet):
    queryset = StaticPage.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = StaticPageSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
