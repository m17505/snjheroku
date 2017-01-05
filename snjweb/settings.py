# -*- coding: utf-8 -*-
"""
Django settings for snjweb project, on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import dj_database_url
gettext = lambda s: s
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DEBUG = False
if not DEBUG:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_SECURE_URLS = True  # use http instead of https
    AWS_QUERYSTRING_AUTH = False  # don't add complex authentication-related query parameters for requests


# Application definition

INSTALLED_APPS = (
    'cms',  # django CMS itself
    'treebeard',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for JavaScript and CSS management
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_picture',
    'featurebox',
    'frontslide',
    'storages',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'snjweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # ...
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

WSGI_APPLICATION = 'snjweb.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


CMS_TEMPLATES = (
    ('template_1.html', 'Home Template'),
    ('template_2.html', 'Collections'),
)

LANGUAGES = [
    ('en-us', 'EN'),
    ('el-gr', 'GR'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_ALIASES = {
    '': {
        'featurebox': {'size': (235, 235), 'crop': True},
    },
}

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

CMS_ENABLE_UPDATE_CHECK = False
IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'
IMAGE_CROPPING_BACKEND_PARAMS = {}

if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': '5432',
        }
    }

    # Update database configuration with $DATABASE_URL.

    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

    SITE_ID = 1

    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, 'static'),
    )

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % os.environ.get('AWS_STORAGE_BUCKET_NAME')

    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'snjweb.s3utils.StaticRootS3BotoStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'snjweb.s3utils.MediaRootS3BotoStorage'
