# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
        ('hosting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='hosting',
            field=models.ForeignKey(to='hosting.Hosting'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domain',
            name='parent_domain',
            field=models.ForeignKey(related_name='parent_domain_rel', blank=True, to='domain.Domain', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='domain',
            unique_together=set([('domain',)]),
        ),
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
