# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_remove_signup_choics'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='choics',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
