from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from featurebox.models import FeatureBox as FeatureBoxModel
from django.utils.translation import ugettext_lazy as _
from image_cropping import ImageCroppingMixin

class FeatureBoxPlugin(ImageCroppingMixin, CMSPluginBase):
    model = FeatureBoxModel
    render_template = "featurebox/plugin.html"
    name = _("Feature Box Plugin")
    cache = False
    render_plugin = True

    def render(self, context, instance, placeholder):
        #context = super(FeatureBoxPlugin, self).render(context, instance, placeholder)
        context['instance'] = instance
        return context

plugin_pool.register_plugin(FeatureBoxPlugin)