from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _tr
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from parler.models import TranslatableModel, TranslatedFields
from page.models import seo_translations, SEOStarterModel
from utils.models import BannerStarterModel


class PricingPlan(TranslatableModel, SEOStarterModel, BannerStarterModel):
    translations = TranslatedFields(
        name=models.CharField(_("Name"), max_length=100),
        page_title=models.CharField(
            _("Page Title"), max_length=200, blank=True, null=True
        ),
        content=RichTextUploadingField(_("Page Content"), blank=True, null=True),
        **BannerStarterModel.translations,
        **seo_translations,
    )
    order = models.IntegerField(_("Ordering"), default=0)
    is_special = models.BooleanField(_("Is Special?"), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Pricing Plan")
        verbose_name_plural = _("Pricing Plans")
        ordering = ("order",)

    def get_absolute_url(self):
        # Pricing plan URLs removed from site
        return "#"


class PricingPlanFeature(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Name"), max_length=100),
    )
    plan = models.ForeignKey(
        PricingPlan,
        on_delete=models.CASCADE,
        verbose_name=_("Pricing Plan"),
        related_name="features",
    )
    is_checked = models.BooleanField(_("Is Checked?"), default=True)
    order = models.IntegerField(_("Ordering"), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Pricing Plan Feature")
        verbose_name_plural = _("Pricing Plan Features")
        ordering = ("order",)


class PricesPageSeo(TranslatableModel, SEOStarterModel, BannerStarterModel):
    translations = TranslatedFields(
        title=models.CharField(_("Page Title"), max_length=200, blank=True, null=True),
        content=RichTextUploadingField(_("Content"), blank=True, null=True),
        **BannerStarterModel.translations,
        **seo_translations,
    )

    class Meta:
        verbose_name = _("Prices Page SEO")
        verbose_name_plural = _("Prices Page SEO")

    def __str__(self):
        return _tr("Prices Page SEO")


class PriceServiceCategory(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=100),
        slug=models.SlugField(_("Slug"), max_length=100),
        description=models.TextField(_("Description"), blank=True, null=True),
    )
    order = models.IntegerField(_("Ordering"), default=0)

    class Meta:
        verbose_name = _("Price Service Category")
        verbose_name_plural = _("Price Service Categories")
        ordering = ("order",)

    def __str__(self):
        return self.title


class PriceServiceItem(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200, blank=True, null=True),
        content=RichTextUploadingField(_("Content"), blank=True, null=True),
    )
    page = models.ForeignKey(PricesPageSeo, on_delete=models.CASCADE)
    category = models.ForeignKey(
        PriceServiceCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    price = models.CharField(_("Price"), max_length=50)
    order = models.IntegerField(_("Ordering"), default=0)

    class Meta:
        verbose_name = _("Price Service Item")
        verbose_name_plural = _("Price Service Items")
        ordering = ("order",)

    def __str__(self):
        return self.title
