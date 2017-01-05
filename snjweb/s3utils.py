from storages.backends.s3boto import S3BotoStorage

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
# MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')
class MediaS3BotoStorage(S3BotoStorage):
    location = 'media'
