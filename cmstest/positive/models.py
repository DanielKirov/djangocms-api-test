from django.db import models
from cms.models.pluginmodel import CMSPlugin
# Create your models here.

class TextInception(CMSPlugin):

    normal_text = models.CharField(max_length=200)

