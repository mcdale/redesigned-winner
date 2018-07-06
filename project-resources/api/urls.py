from django.conf import settings
from django.conf.urls import include, url
from rest_framework import routers

from .views import (
    ProjectViewSet
)

router = routers.DefaultRouter()

router.register(r'projects', ProjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
