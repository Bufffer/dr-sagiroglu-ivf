from django.db import models
from django.utils.translation import gettext as _tr
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField

from page.models import seo_translations, SEOStarterModel


class HomePageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(
        **seo_translations,
    )

    def __str__(self):
        return _tr("Home SEO")

    class Meta:
        verbose_name = _("Home SEO")
        verbose_name_plural = _("Home SEO")


class BannerSlide(TranslatableModel):
    translations = TranslatedFields(
        maintitle=models.CharField(
            _("Main Title"), blank=True, null=True, max_length=200
        ),
        subtitle=models.CharField(_("Subtitle"), blank=True, null=True, max_length=200),
        description=models.TextField(_("Description"), null=True, blank=True),
        redirect_link=models.CharField(
            _("Redirect Link"),
            blank=True,
            null=True,
            max_length=300,
            help_text="You can enter full url or relative path like '/about'",
        ),
    )
    image = models.ImageField(_("Image"), upload_to="banner/slides")
    order = models.IntegerField(_("Order"), default=0)

    def __str__(self):
        return _("Banner Slider %s") % self.id

    class Meta:
        verbose_name = _("Banner Slider")
        verbose_name_plural = _("Banner Sliders")
        ordering = ("order",)
