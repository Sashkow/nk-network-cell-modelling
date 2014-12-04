# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0007_auto_20141204_0704'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cell',
        ),
    ]
