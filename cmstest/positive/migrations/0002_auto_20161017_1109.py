# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinception',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='positive_textinception', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
