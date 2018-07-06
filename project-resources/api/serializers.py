from datetime import datetime

import rest_framework

from rest_framework_json_api import relations, serializers

from .models import (
    Project,
    TaggedItem
)


class TaggedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedItem
        fields = ('tag',)


class ProjectSerializer(serializers.ModelSerializer):
    copyright = serializers.SerializerMethodField()
    tags = TaggedItemSerializer(many=True, read_only=True)

    include_serializers = {
        'tags': '.serializers.TaggedItemSerializer',
    }

    def get_copyright(self, resource):
        return datetime.now().year

    def get_root_meta(self, resource, many):
        return {
            'api_docs': '/docs/api/projects'
        }

    class Meta:
        model = Project
        fields = ('name', 'url', 'tags')
        read_only_fields = ('tags',)
        meta_fields = ('copyright',)
