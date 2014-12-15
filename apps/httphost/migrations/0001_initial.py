# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HttpHost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('configuration', models.TextField(blank=True)),
                ('php', models.BooleanField(default=False)),
                ('usessl', models.BooleanField(default=False)),
                ('certificate', models.TextField(blank=True)),
                ('certificate_key', models.TextField(blank=True)),
                ('certificate_chain', models.TextField(blank=True)),
                ('certificate_authority', models.TextField(blank=True)),
                ('domain', models.ForeignKey(to='domain.Domain', unique=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
