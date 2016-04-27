# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 20:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_phone_msisdn_validator'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='base_contact_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactphone',
            name='user',
            field=models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='base_contactphone_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logentry',
            name='user',
            field=models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='base_logentry_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
