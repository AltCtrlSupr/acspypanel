# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
        ('dnsdomain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnsdomain',
            name='domain',
            field=models.ForeignKey(to='domain.Domain', unique=True),
        ),
    ]
