# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('domain', models.CharField(unique=True, max_length=255)),
                ('is_httpd_alias', models.BooleanField(default=False)),
                ('is_dns_alias', models.BooleanField(default=False)),
                ('is_mail_alias', models.BooleanField(default=False)),
                ('hosting', models.ForeignKey(to='hosting.Hosting')),
                ('parent_domain', models.ForeignKey(related_name='parent_domain_rel', blank=True, to='domain.Domain', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
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
