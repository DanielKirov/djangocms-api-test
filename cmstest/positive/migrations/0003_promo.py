# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0006_auto_20160623_1627'),
        ('positive', '0002_auto_20161017_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='positive_promo', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('headline', models.CharField(max_length=256)),
                ('subheading', models.CharField(max_length=512, null=True, blank=True)),
                ('image', filer.fields.image.FilerImageField(to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
