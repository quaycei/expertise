# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0008_auto_20170213_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stakeholder_map',
            name='assumptions',
        ),
        migrations.RemoveField(
            model_name='stakeholder_map',
            name='clusters',
        ),
        migrations.RemoveField(
            model_name='stakeholder_map',
            name='entitys',
        ),
        migrations.RemoveField(
            model_name='stakeholder_map',
            name='stakeholders',
        ),
        migrations.AddField(
            model_name='assumption',
            name='stakeholder_map',
            field=models.ManyToManyField(blank=True, default=None, to='stakeholder.Stakeholder_Map'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='stakeholder_map',
            field=models.ManyToManyField(blank=True, default=None, to='stakeholder.Stakeholder_Map'),
        ),
        migrations.AddField(
            model_name='entity',
            name='stakeholder_map',
            field=models.ManyToManyField(blank=True, default=None, to='stakeholder.Stakeholder_Map'),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='stakeholder_map',
            field=models.ManyToManyField(blank=True, default=None, to='stakeholder.Stakeholder_Map'),
        ),
    ]
