# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('account', '0002_account_domain'),
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
        ),
        migrations.CreateModel(
            name='HostingResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('count', models.PositiveIntegerField(default=0)),
                ('hosting', models.ForeignKey(to='hosting.Hosting')),
            ],
            options={
                'abstract': False,
            },
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
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('parent', models.ForeignKey(related_name='parent_resource', to='hosting.Resource')),
            ],
        ),
        migrations.AddField(
            model_name='planresource',
            name='resource',
            field=models.ForeignKey(to='hosting.Resource'),
        ),
        migrations.AddField(
            model_name='plan',
            name='resources',
            field=models.ManyToManyField(to='hosting.Resource', through='hosting.PlanResource'),
        ),
        migrations.AddField(
            model_name='hostingresource',
            name='resource',
            field=models.ForeignKey(to='hosting.Resource'),
        ),
        migrations.AddField(
            model_name='hostingplan',
            name='plan',
            field=models.ForeignKey(to='hosting.Plan'),
        ),
        migrations.AddField(
            model_name='hosting',
            name='plan',
            field=models.ManyToManyField(to='hosting.Plan', through='hosting.HostingPlan'),
        ),
        migrations.AddField(
            model_name='hosting',
            name='resource',
            field=models.ManyToManyField(to='hosting.Resource', through='hosting.HostingResource'),
        ),
        migrations.AlterUniqueTogether(
            name='resource',
            unique_together=set([('name', 'content_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='hosting',
            unique_together=set([('name',)]),
        ),
    ]
