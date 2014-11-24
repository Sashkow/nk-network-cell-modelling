# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cell',
            old_name='K',
            new_name='k',
        ),
        migrations.RenameField(
            model_name='cell',
            old_name='N',
            new_name='n',
        ),
        migrations.AddField(
            model_name='cell',
            name='serizlized_object',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
