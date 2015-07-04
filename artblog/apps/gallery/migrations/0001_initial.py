# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageEntry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('caption', models.TextField()),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Images',
                'ordering': ['-uploaded'],
                'verbose_name': 'Image',
            },
        ),
    ]
