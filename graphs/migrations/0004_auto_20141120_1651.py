# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0003_auto_20141120_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cell',
            old_name='serizlized_object',
            new_name='serialized_object',
        ),
    ]
