# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-28 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_jects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(),
        ),
    ]