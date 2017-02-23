# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopefear', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='emotion',
            field=models.IntegerField(choices=[('0', 'Undeclared'), ('1', 'Hope'), ('2', 'Fear')], default=0),
        ),
    ]
