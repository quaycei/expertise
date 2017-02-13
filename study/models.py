from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_slug

class Study(models.Model):
    creator = models.ForeignKey(User, default=None)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(default=None, blank=True)
