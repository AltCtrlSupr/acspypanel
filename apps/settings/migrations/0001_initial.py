# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('required', models.BooleanField(default=False)),
                ('type', models.CharField(default=b'string', max_length=10, choices=[(b'string', b'String'), (b'check', b'Check Box'), (b'int', b'Integer'), (b'model', b'Model')])),
                ('string_value', models.CharField(max_length=255, null=True, blank=True)),
                ('int_value', models.IntegerField(null=True, blank=True)),
                ('bool_value', models.NullBooleanField()),
                ('scope', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='SettingValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('string_value', models.CharField(max_length=255, null=True, blank=True)),
                ('int_value', models.IntegerField(null=True, blank=True)),
                ('bool_value', models.NullBooleanField()),
                ('use_default', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField()),
                ('key', models.ForeignKey(to='settings.SettingKey')),
                ('scope', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
