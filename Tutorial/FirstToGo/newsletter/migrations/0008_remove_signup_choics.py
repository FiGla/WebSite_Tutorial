# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_signup_choics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='choics',
        ),
    ]
