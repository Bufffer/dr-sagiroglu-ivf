from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _tr
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import switch_language

from page.models import seo_translations, SEOStarterModel
from utils.models import BannerStarterModel


class JourneyPageSeo(TranslatableModel, SEOStarterModel, BannerStarterModel):
    translations = TranslatedFields(
        **BannerStarterModel.translations,
        **seo_translations,
    )

    class Meta:
        verbose_name = _("Journey Page SEO")
        verbose_name_plural = _("Journey Page SEO")

    def __str__(self):
        return _tr("Journey Page SEO")


class JourneyItem(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=100),
        slug=models.SlugField(_("Slug"), max_length=100),
        content=RichTextUploadingField(_("Content"), blank=True, null=True),
        description=models.TextField(_("Description"), blank=True, null=True),
    )
    image = models.ImageField(
        _("Image"), upload_to="journey", blank=True, null=True
    )

    class Meta:
        verbose_name = _("Journey Item")
        verbose_name_plural = _("Journey Items")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        with switch_language(self):
            path = reverse("journey")
            return f"{path}?item={self.slug}"
