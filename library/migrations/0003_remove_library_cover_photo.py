# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_library_cover_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='cover_photo',
        ),
    ]