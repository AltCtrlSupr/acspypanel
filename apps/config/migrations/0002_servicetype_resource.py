# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0002_auto_20150930_2040'),
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='resource',
            field=models.ForeignKey(blank=True, to='hosting.Resource', null=True),
        ),
    ]
