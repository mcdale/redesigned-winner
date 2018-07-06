import rest_framework.parsers
import rest_framework.renderers
from rest_framework import exceptions

import rest_framework_json_api.metadata
import rest_framework_json_api.parsers
import rest_framework_json_api.renderers
from rest_framework_json_api.pagination import PageNumberPagination
from rest_framework_json_api.utils import format_drf_errors
from rest_framework_json_api.views import ModelViewSet, RelationshipView

from .models import (
    Project,
    TaggedItem
)

from .serializers import (
    ProjectSerializer,
    TaggedItemSerializer
)

HTTP_422_UNPROCESSABLE_ENTITY = 422

# Create your views here.
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
