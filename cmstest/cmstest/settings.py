# -*- coding: utf-8 -*-
import os
from django.core.exceptions import ImproperlyConfigured


def _get_env_variable(var_name, default=None):
    """
    Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        if default:
            return default
        else:
            error_msg = "Set the %s env variable" % var_name
            raise ImproperlyConfigured(error_msg)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5u%*r&rn1z$x8!%!+6p*y^ayvz55@3704xgvkl8#4avl*ndh4^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cms',  # django CMS itself
    'treebeard',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for JavaScript and CSS management
    'djangocms_admin_style',
    # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
    'djangocms_link',
    'cmsplugin_filer_image',
    'djangocms_text_ckeditor',
    'positive',
    'easy_thumbnails',
    'filer',
    'mptt',
    'rest_framework',
    'djangocms_rest_api',
    'reversion',
    'rest_framework_recursive',
)

MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

ROOT_URLCONF = 'cmstest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'cmstest.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': _get_env_variable('POSTGRES_DB', default='cmstest'),
        'USER': _get_env_variable('POSTGRES_USER', default='vagrant'),
        'PASSWORD': _get_env_variable('POSTGRES_PASSWORD', default='vagrant'),
        'HOST': _get_env_variable('POSTGRES_HOST', default='localhost'),
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

LANGUAGES = [
    ('en-gb', 'English'),
]

SITE_ID = 1

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
)

CKEDITOR_SETTINGS = {
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format'],
        ['NumberedList', 'BulletedList'],
        ['Bold', 'Italic', 'RemoveFormat'],
    ],
}


CMS_PERMISSION = True