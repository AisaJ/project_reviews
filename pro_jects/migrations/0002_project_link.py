# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-29 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_jects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default='site.com', max_length=60),
        ),
    ]
