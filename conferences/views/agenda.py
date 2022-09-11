from rest_framework import viewsets
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.talks import Talk
from conferences.serializers.talks import TalkSerializer
from rest_framework.generics import ListAPIView


class AgendaViewSet(ListAPIView):
    queryset = Talk.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = self.queryset
        return queryset
