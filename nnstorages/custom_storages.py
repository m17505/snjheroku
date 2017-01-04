# custom_storages.py
from snjweb.settings import *
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    location = STATICFILES_LOCATION

class MediaStorage(S3BotoStorage):
    location = MEDIAFILES_LOCATION
