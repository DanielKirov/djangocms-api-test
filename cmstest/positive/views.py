from django.shortcuts import render
from djangocms_rest_api import serializers
from django.http import HttpResponse, JsonResponse
from djangocms_text_ckeditor.models import Text
from .serializers import TextPluginSerializer
from django.template import RequestContext

def textplugin_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        text_plugin = Text.objects.get(pk=pk)
    except Text.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        context = RequestContext(request)
        context['request'] = request
        serializer = TextPluginSerializer(text_plugin, context=context)
        return JsonResponse(serializer.data)