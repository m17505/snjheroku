# -*- coding: utf-8 -*-
from snjweb.settings_base import *

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'snjdb',
        'USER': 'snjdb',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

STATICFILES_DIRS = (
  os.path.join(PROJECT_ROOT, 'static'),
)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
MEDIA_URL = "/media/"

SITE_ID = 2
