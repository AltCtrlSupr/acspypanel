# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='parent',
            field=models.ForeignKey(related_name='parent_resource', blank=True, to='hosting.Resource', null=True),
        ),
    ]
