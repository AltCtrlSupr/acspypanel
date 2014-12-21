# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='adminuser',
            field=models.OneToOneField(related_name='adminuser', blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
