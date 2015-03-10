# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0004_auto_20150309_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostingResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('count', models.PositiveIntegerField(default=0)),
                ('hosting', models.ForeignKey(to='hosting.Hosting')),
                ('resource', models.ForeignKey(to='hosting.Resource')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='hosting',
            name='used_resource',
        ),
        migrations.AddField(
            model_name='hosting',
            name='resource',
            field=models.ManyToManyField(to='hosting.Resource', through='hosting.HostingResource'),
            preserve_default=True,
        ),
    ]
