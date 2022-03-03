from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from conferences.models.static_pages import StaticPage


class StaticPageSerializer(ModelSerializer):
    class Meta:
        model = StaticPage
        fields = (
            "id",
            "title",
            "content",
            "format",
            "rendered_content",
            "published",
        )
