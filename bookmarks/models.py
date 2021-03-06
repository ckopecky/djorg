"""Django models for Bookmarks app"""
from uuid import uuid4
from django.db import models

# Create your models here.
class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    notes = models.TextField('Notes', blank=True)
    url = models.URLField('URL', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # Todo add tags and isfavorite
    #tags = models.ManyToManyField(Tag)

class Tag(models.Model):
	'''Creates Tags for Bookmarks'''
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	name = models.CharField(max_length=30)
