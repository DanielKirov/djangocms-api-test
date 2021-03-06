"""
WSGI config for cmstest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import sys
import os
sys.path.insert(0, 'djangocms-rest-api/')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmstest.settings")

application = get_wsgi_application()
