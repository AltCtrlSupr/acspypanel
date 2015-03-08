# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
        ('account', '0001_initial'),
        ('hosting', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='domain',
            field=models.ForeignKey(blank=True, to='domain.Domain', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='hosting',
            field=models.ForeignKey(blank=True, to='hosting.Hosting', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
