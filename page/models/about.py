from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _tr

from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel
from page.models.faqs import faqs_fields

from utils.models import BannerStarterModel


class BaseAboutPage(SEOStarterModel, BannerStarterModel):
    translations = dict(
        **BannerStarterModel.translations,
        **seo_translations,
        subtitle=models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Subtitle")),
        title=models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Title")),
        content=RichTextField(blank=True, null=True, verbose_name=_("Content")),
        **faqs_fields,
    )
    youtube_link = models.URLField(blank=True, null=True, verbose_name=_("Youtube Link"))
    image = models.ImageField(_("Image"), upload_to="about", blank=True, null=True)

    class Meta:
        abstract = True


class AboutPageSeo(TranslatableModel, BaseAboutPage):
    translations = TranslatedFields(
        **BaseAboutPage.translations
    )

    class Meta:
        verbose_name = _("About Page SEO")
        verbose_name_plural = _("About Page SEO")

    def __str__(self):
        return _tr("About Page SEO")


class AboutDoctorPageSeo(TranslatableModel, BaseAboutPage):
    translations = TranslatedFields(
        **BaseAboutPage.translations,
    )

    class Meta:
        verbose_name = _("Cengiz Sagiroglu Page SEO")
        verbose_name_plural = _("Cengiz Sagiroglu Page SEO")

    def __str__(self):
        return _tr("Cengiz Sagiroglu Page SEO")


class JineartClinicPageSeo(TranslatableModel, BaseAboutPage):
    # WhyUsPageSeo
    translations = TranslatedFields(
        **BaseAboutPage.translations,
    )

    class Meta:
        verbose_name = _("Why Us Page SEO")
        verbose_name_plural = _("Why Us Page SEO")

    def __str__(self):
        return _tr("Why Us Page SEO")


class JineartLabPageSeo(TranslatableModel, BaseAboutPage):
    # SuccessRatesPageSeo
    translations = TranslatedFields(
        **BaseAboutPage.translations,
    )

    class Meta:
        verbose_name = _("Success Rates Page SEO")
        verbose_name_plural = _("Success Rates Page SEO")

    def __str__(self):
        return _tr("Success Rates Page SEO")


class HowItWorksPageSeo(TranslatableModel, SEOStarterModel, BannerStarterModel):
    translations = TranslatedFields(
        **BannerStarterModel.translations,
        **seo_translations,
        subtitle1=models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Subtitle 1")),
        title1=models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Title 1")),
        content1=RichTextField(blank=True, null=True, verbose_name=_("Content 1")),
        subtitle2=models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Subtitle 2")),
        title2=models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Title 2")),
        content2=RichTextField(blank=True, null=True, verbose_name=_("Content 2")),
        subtitle3=models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Subtitle 3")),
        title3=models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Title 3")),
        content3=RichTextField(blank=True, null=True, verbose_name=_("Content 3")),
        **faqs_fields,

    )
    image1 = models.ImageField(upload_to="how_it_works/", verbose_name=_("Image 1"), blank=True, null=True)
    image2 = models.ImageField(upload_to="how_it_works/", verbose_name=_("Image 2"), blank=True, null=True)
    image3 = models.ImageField(upload_to="how_it_works/", verbose_name=_("Image 3"), blank=True, null=True)

    class Meta:
        verbose_name = _("Plan Your Journey Page SEO")
        verbose_name_plural = _("Plan Your Journey Page SEO")

    def __str__(self):
        return _tr("Plan Your Journey Page SEO")
