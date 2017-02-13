from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_slug


class Cluster(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])
    name = models.CharField(max_length=150, default=None, blank=False)
    tagline = models.CharField(max_length=150, blank=True, default=None)
    description = models.TextField(max_length=500, default=None, blank=True)

    def __str__(self):
        return self.name
    

class Entity(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])
    clusters = models.ManyToManyField(Cluster, default=None, blank=True)
    name = models.CharField(max_length=150, default=None, blank=False)
    description = models.TextField(max_length=500, default=None, blank=True)

    def __str__(self):
        return self.name
    


class Stakeholder(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])
    entity = models.ForeignKey(Entity, default=None, blank=True)
    clusters = models.ManyToManyField(Cluster, default=None, blank=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=150, blank=True, default=None)
    tagline = models.CharField(max_length=150, blank=True, default=None)
    email_address = models.CharField(max_length=150, blank=True, default=None)
    phone_number = models.CharField(max_length=150, blank=True, default=None)
    website = models.CharField(max_length=150, blank=True, default=None)

    def __str__(self):
        return self.name
    

class Assumption(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])
    stakeholders = models.ManyToManyField(Stakeholder, default=None, blank=True)
    entitys = models.ManyToManyField(Entity, default=None, blank=True)
    clusters = models.ManyToManyField(Cluster, default=None, blank=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=150, blank=True, default=None)
    tagline = models.CharField(max_length=150, blank=True, default=None)
    proven = models.BooleanField(default=None)
    
    def __str__(self):
        return self.name


class Stakeholder_Map(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])
    name = models.CharField(max_length=150, default=None, blank=False)
    tagline = models.CharField(max_length=150, blank=True, default=None)
    description = models.TextField(max_length=500, default=None, blank=True)
    hex_color = models.CharField(max_length=7, blank=True, default="#4DB6AC")
    stakeholders = models.ManyToManyField(Stakeholder, default=None, blank=True)
    entitys = models.ManyToManyField(Entity, default=None, blank=True)
    clusters = models.ManyToManyField(Cluster, default=None, blank=True)
    assumptions = models.ManyToManyField(Assumption, default=None, blank=True)

    def __str__(self):
        return self.name

