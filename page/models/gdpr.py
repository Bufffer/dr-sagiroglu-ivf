from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor_uploader.fields import RichTextUploadingField

from page.models import seo_translations, SEOStarterModel
from utils.models import BannerStarterModel


class GDPRPageSeo(TranslatableModel, SEOStarterModel, BannerStarterModel):
    translations = TranslatedFields(
        content=RichTextUploadingField(_("Content"), blank=True, null=True),
        **BannerStarterModel.translations,
        **seo_translations
    )

    class Meta:
        verbose_name = _("GDPR Page SEO")
        verbose_name_plural = _("GDPR Page SEO")


class PrivacyPageSeo(TranslatableModel, SEOStarterModel, BannerStarterModel):
    translations = TranslatedFields(
        content=RichTextUploadingField(_("Content"), blank=True, null=True),
        **BannerStarterModel.translations,
        **seo_translations
    )

    class Meta:
        verbose_name = _("Privacy Page SEO")
        verbose_name_plural = _("Privacy Page SEO")
