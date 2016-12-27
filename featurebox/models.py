from django.db import models
from cms.models.pluginmodel import CMSPlugin
from image_cropping import ImageRatioField, ImageCropField
from cms.models.fields import PageField


class FeatureBox(CMSPlugin):
    # image = ThumbnailerImageField(upload_to='featurebox', blank=False)
    image = ImageCropField(upload_to='featurebox', blank=False)
    # size is "width x height"
    cropping = ImageRatioField('image', '360x360')
    text = models.TextField()
    page_link = PageField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
