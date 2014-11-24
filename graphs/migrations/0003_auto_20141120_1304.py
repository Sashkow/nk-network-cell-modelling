# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0002_auto_20141120_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell',
            name='serizlized_object',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
