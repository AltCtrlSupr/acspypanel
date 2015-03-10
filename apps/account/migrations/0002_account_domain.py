# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='domain',
            field=models.ForeignKey(blank=True, to='domain.Domain', null=True),
            preserve_default=True,
        ),
    ]
