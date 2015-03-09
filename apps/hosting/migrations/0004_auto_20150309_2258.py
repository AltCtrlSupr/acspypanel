# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0003_hosting_used_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosting',
            name='used_resource',
            field=models.TextField(default={}),
            preserve_default=True,
        ),
    ]
