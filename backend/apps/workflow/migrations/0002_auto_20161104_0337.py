# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-04 03:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='epstatus',
            old_name='task_id',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='epstatus',
            old_name='workflow_id',
            new_name='workflow',
        ),
        migrations.RenameField(
            model_name='eptask',
            old_name='workflow_id',
            new_name='workflow',
        ),
        migrations.RenameField(
            model_name='epworkflow',
            old_name='company_id',
            new_name='company',
        ),
    ]
