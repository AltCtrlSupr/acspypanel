# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainWizard',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('domain.domain',),
        ),
    ]
