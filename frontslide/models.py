from django.db import models
from cms.models.pluginmodel import CMSPlugin
from image_cropping import ImageRatioField, ImageCropField
from cms.models.fields import PageField


class FrontSlide(CMSPlugin):
    image = ImageCropField(upload_to='featurebox', blank=False)
    normal_slide_crop = ImageRatioField('image', '1920x1160')
    mobile_slide_crop = ImageRatioField('image', '410x314')
    text = models.TextField()
    page_link = PageField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
