# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0002_auto_20150309_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosting',
            name='used_resource',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
