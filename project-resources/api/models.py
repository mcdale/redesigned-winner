from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TaggedItem(BaseModel):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ('id',)


class Project(BaseModel):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    tags = GenericRelation(TaggedItem)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
