# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEditPro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('bio', models.TextField(null=True, blank=True)),
                ('contect', models.CharField(max_length=15, null=True, blank=True)),
                ('user', models.OneToOneField(to='blog.Register')),
            ],
        ),
    ]
