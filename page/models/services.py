from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _tr
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import switch_language

from page.models import seo_translations, SEOStarterModel
from page.models.faqs import faqs_fields
from utils.models import TimestampStarterModel, BannerStarterModel


class ServicesPageSeo(TranslatableModel, SEOStarterModel, BannerStarterModel):
    translations = TranslatedFields(
        **BannerStarterModel.translations,
        **seo_translations,
    )

    class Meta:
        verbose_name = _("Services Page SEO")
        verbose_name_plural = _("Services Page SEO")

    def __str__(self):
        return _tr("Services Page SEO")


class ServiceCategory(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=100),
        slug=models.SlugField(_("Slug"), max_length=100),
    )

    class Meta:
        verbose_name = _("Service Category")
        verbose_name_plural = _("Service Categories")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        with switch_language(self):
            path = reverse("services")
            return f"{path}?category={self.slug}"


class ServiceItem(TranslatableModel, SEOStarterModel, BannerStarterModel, TimestampStarterModel):
    translations = TranslatedFields(
        **BannerStarterModel.translations,
        **seo_translations,
        title=models.CharField(_("Title"), max_length=200),
        slug=models.SlugField(_("Slug"), max_length=200),
        description=RichTextField(verbose_name=_("Description"), blank=True, null=True),
        content=RichTextUploadingField(_("Content"), blank=True, null=True),
        **faqs_fields,
    )
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Category"),
        related_name="service_items",
    )
    image = models.ImageField(
        _("Image"), upload_to="services", blank=True, null=True
    )
    icon = models.ImageField(_("Icon"), upload_to="services/icons", blank=True, null=True)
    in_navbar = models.BooleanField(default=False, verbose_name=_("In Navigation?"))
    in_home = models.BooleanField(default=False, verbose_name=_("In Home Page?"))
    in_about_page = models.BooleanField(default=False, verbose_name=_("In About Page?"))
    in_doctor_page = models.BooleanField(default=False, verbose_name=_("In Cengiz Sagiroglu Page?"))
    order = models.IntegerField(_("Ordering"), default=0)

    class Meta:
        verbose_name = _("Service Item")
        verbose_name_plural = _("Service Items")
        ordering = ("order", "id")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        with switch_language(self):
            return reverse("services_detail", args=(self.slug,))
