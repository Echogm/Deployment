# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171025_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelers',
            name='travelers',
        ),
    ]
