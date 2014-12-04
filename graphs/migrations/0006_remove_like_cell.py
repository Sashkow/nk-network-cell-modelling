# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0005_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='cell',
        ),
    ]
