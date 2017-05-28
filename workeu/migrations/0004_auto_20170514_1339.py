# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workeu', '0003_postf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postf',
            old_name='text_f',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='postf',
            old_name='title_f',
            new_name='title',
        ),
    ]
