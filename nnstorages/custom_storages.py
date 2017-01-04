# custom_storages.py
from django.conf import settings
# from storages.backends.s3boto import S3BotoStorage


class StaticStorage(storages.backends.s3boto.S3BotoStorage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(storages.backends.s3boto.S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
