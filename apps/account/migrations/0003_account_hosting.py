# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0001_initial'),
        ('account', '0002_account_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='hosting',
            field=models.ForeignKey(blank=True, to='hosting.Hosting', null=True),
            preserve_default=True,
        ),
    ]
