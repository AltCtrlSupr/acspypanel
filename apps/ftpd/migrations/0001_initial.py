# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FtpdUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uid', models.IntegerField(null=True, blank=True)),
                ('gid', models.IntegerField(null=True, blank=True)),
                ('dir', models.CharField(default=b'/', max_length=255)),
                ('quota', models.IntegerField(null=True, blank=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('username', models.OneToOneField(to='account.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
