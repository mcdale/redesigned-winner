from django.contrib import admin
from .models import Project, TaggedItem

# Register your models here.
MODELS = [
    Project,
    TaggedItem,
]

admin.site.register(MODELS)
