from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_slug




class Library(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])
    name = models.CharField(max_length=150, default=None, blank=False)
    tagline = models.CharField(max_length=150, blank=True, default=None)
    description = models.TextField(max_length=500, default=None, blank=True)
    hex_color = models.CharField(max_length=7, blank=True, default="#4DB6AC")

    def __str__(self):
        return self.name


class Project(models.Model):
    creator = models.ForeignKey(User, default=None)
    library = models.ManyToManyField(Library, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])
    name = models.CharField(max_length=150, default=None, blank=False)
    tagline = models.CharField(max_length=150, blank=True, default=None)
    description = models.TextField(max_length=500, default=None, blank=True)
    hex_color = models.CharField(max_length=7, blank=True, default="#4DB6AC")

    def __str__(self):
        return self.name



