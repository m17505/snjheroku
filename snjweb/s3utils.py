import os
from storages.backends.s3boto import S3BotoStorage

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_S3_SECURE_URLS = True  # use http instead of https
AWS_QUERYSTRING_AUTH = False  # don't add complex authentication-related query parameters for requests

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')
