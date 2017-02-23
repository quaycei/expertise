from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_slug
from library.models import Library, Project




class Hopefear_Map(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    library = models.ManyToManyField(Library, default=None, blank=True)
    project = models.ManyToManyField(Project, default=None, blank=True)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])
    name = models.CharField(max_length=150, default=None, blank=False)
    tagline = models.CharField(max_length=150, blank=True, default=None)
    description = models.TextField(max_length=500, default=None, blank=True)
    hex_color = models.CharField(max_length=7, blank=True, default="#4DB6AC")

    def __str__(self):
        return self.name



class Thought(models.Model):
    EMOTION_CHOICES = (
     (1, 'Undeclared'),
     (2, 'Hope'),
     (3, 'Fear'),
    )
    hopefear_map = models.ForeignKey(Hopefear_Map, default=None)
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=150, default=None, blank=False)
    tagline = models.CharField(max_length=150, blank=True, default=None)
    description = models.TextField(max_length=500, default=None, blank=True)
    emotion = models.IntegerField(choices=EMOTION_CHOICES, default=0)

    def __str__(self):
        return self.name





