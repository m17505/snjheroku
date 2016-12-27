from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from frontslide.models import FrontSlide as FrontSlideModel
from django.utils.translation import ugettext_lazy as _
from image_cropping import ImageCroppingMixin

class FrontSlidePlugin(ImageCroppingMixin, CMSPluginBase):
    model = FrontSlideModel
    render_template = "frontslide/plugin.html"
    name = _("FrontSlide Plugin")
    cache = False
    render_plugin = True

    def render(self, context, instance, placeholder):
        #context = super(FeatureBoxPlugin, self).render(context, instance, placeholder)
        context['instance'] = instance
        return context

plugin_pool.register_plugin(FrontSlidePlugin)