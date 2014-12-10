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
            old_name='serialized_object',
            new_name='pickled_automata',
        ),
    ]
