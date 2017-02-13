# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 19:40
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stakeholder', '0003_auto_20170212_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.CharField(max_length=21, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, default=None, max_length=150)),
                ('tagline', models.CharField(blank=True, default=None, max_length=150)),
                ('proven', models.BooleanField(default=None)),
                ('creator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('stakeholders', models.ManyToManyField(to='stakeholder.Stakeholder')),
            ],
        ),
    ]
