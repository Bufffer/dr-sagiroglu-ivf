from django.utils.translation import ugettext as _tr
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel
from utils.models import BannerStarterModel


class ContactPageSeo(TranslatableModel, SEOStarterModel, BannerStarterModel):
    translations = TranslatedFields(
        **BannerStarterModel.translations,
        **seo_translations
    )

    class Meta:
        verbose_name = _("Contact Page SEO")
        verbose_name_plural = _("Contact Page SEO")

    def __str__(self):
        return _tr("Contact Page Seo")
