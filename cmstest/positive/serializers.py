from rest_framework import serializers
from .models import Promo
from djangocms_text_ckeditor.models import Text

class PromoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promo
        depth = 1


class TextPluginSerializer(serializers.ModelSerializer):
    rendered_plugin = serializers.SerializerMethodField()

    def get_rendered_plugin(self, obj):
        from cms.plugin_rendering import ContentRenderer
        request = self._context.request
        renderer = ContentRenderer(request)
        # Avoid errors if plugin require a request object
        # when rendering.
        return renderer.render_plugin(obj, self.context)

    class Meta:
        model = Text
        depth = 1
