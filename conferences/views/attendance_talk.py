from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from conferences.models.attendance_talk import AttendanceTalk
from conferences.serializers.attendance_talk import AttendanceTalkSerializer


class AttendanceTalkViewSet(viewsets.ModelViewSet):
    queryset = AttendanceTalk.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AttendanceTalkSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
