# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to=b'gallery_covers', verbose_name=b'Cover Image')),
            ],
            options={
                'ordering': ('-date',),
                'abstract': False,
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'gallery_images')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Gallery')),
            ],
        ),
    ]