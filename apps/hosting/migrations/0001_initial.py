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
            name='Hosting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(related_name='hosting_owner', to='account.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostingPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hosting', models.ForeignKey(to='hosting.Hosting')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.IntegerField(null=True, blank=True)),
                ('plan', models.ForeignKey(to='hosting.Plan')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('default', models.IntegerField(null=True, blank=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='planresource',
            name='resource',
            field=models.ForeignKey(to='hosting.Resource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planresource',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='resources',
            field=models.ManyToManyField(to='hosting.Resource', through='hosting.PlanResource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hostingplan',
            name='plan',
            field=models.ForeignKey(to='hosting.Plan'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hostingplan',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hosting',
            name='plan',
            field=models.ManyToManyField(to='hosting.Plan', through='hosting.HostingPlan'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hosting',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
