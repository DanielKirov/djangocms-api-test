from django.db import models
from cms.models.pluginmodel import CMSPlugin
from cmsplugin_filer_image.models import FilerImageField


# Create your models here.

class TextInception(CMSPlugin):
    normal_text = models.CharField(max_length=200)


class Promo(CMSPlugin):
    headline = models.CharField(max_length=256)
    subheading = models.CharField(max_length=512, null=True, blank=True)
    image = FilerImageField()
