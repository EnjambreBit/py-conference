from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
# from rest_framework_json_api.relations import ResourceRelatedField

from conferences.models.static_pages import StaticPage


class StaticPageSerializer(ModelSerializer):
    class Meta:
        model = StaticPage
        fields = (
            'id',
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
