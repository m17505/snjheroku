from django.contrib import admin
from image_cropping import ImageCroppingMixin
from featurebox.models import FeatureBox

class FeatureBoxAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(FeatureBox, FeatureBoxAdmin)