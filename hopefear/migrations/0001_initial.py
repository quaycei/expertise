# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 04:40
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hopefear_Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.CharField(max_length=21, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('name', models.CharField(default=None, max_length=150)),
                ('tagline', models.CharField(blank=True, default=None, max_length=150)),
                ('description', models.TextField(blank=True, default=None, max_length=500)),
                ('hex_color', models.CharField(blank=True, default='#4DB6AC', max_length=7)),
                ('creator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('library', models.ManyToManyField(blank=True, default=None, to='library.Library')),
                ('project', models.ManyToManyField(blank=True, default=None, to='library.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default=None, max_length=150)),
                ('tagline', models.CharField(blank=True, default=None, max_length=150)),
                ('description', models.TextField(blank=True, default=None, max_length=500)),
                ('emotion', models.IntegerField(choices=[(1, 'Undeclared'), (2, 'Hope'), (3, 'Fear')], default=0)),
                ('creator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hopefear_map', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hopefear.Hopefear_Map')),
            ],
        ),
    ]