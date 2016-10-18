from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from djangocms_text_ckeditor.cms_plugins import TextPlugin
from django.utils.translation import ugettext_lazy as _

from .models import TextInception

class TextInceptionPlugin(CMSPluginBase):
    model = TextInception
    render_template = "text_inception_plugin.html"
    cache = False
    allow_children = True
    child_classes = ['TextPlugin']

plugin_pool.register_plugin(TextInceptionPlugin)