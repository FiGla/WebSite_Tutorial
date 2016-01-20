# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0011_auto_20160113_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='choics',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
