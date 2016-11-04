# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-04 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='epaccountcompany',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='epaccountcompany',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='epaccountcompany',
            old_name='position_id',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='epposition',
            old_name='company_id',
            new_name='company',
        ),
        migrations.AddField(
            model_name='epaccountcompany',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='epcompany',
            name='members',
            field=models.ManyToManyField(through='account.EPAccountCompany', to='account.EPAccount'),
        ),
    ]
