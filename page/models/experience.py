from django.db import models
from django.utils.translation import ugettext as _tr
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel
from utils.models import BannerStarterModel


class ExperiencePageSeo(TranslatableModel, SEOStarterModel, BannerStarterModel):
    translations = TranslatedFields(
        **BannerStarterModel.translations,
        **seo_translations,
    )

    class Meta:
        verbose_name = _("Experience Page SEO")
        verbose_name_plural = _("Experience Page SEO")

    def __str__(self):
        return _tr("Experience Page SEO")


class ExperienceCategory(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(verbose_name=_("Title"), max_length=100),
        slug=models.SlugField(max_length=100, verbose_name=_("Slug"))
    )

    class Meta:
        verbose_name = _("Experience Category")
        verbose_name_plural = _("Experience Categories")

    def __str__(self):
        return self.title


class ExperienceItem(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=100),
    image = models.ImageField(_("Image"), upload_to="experience", blank=True, null=True)
    category = models.ForeignKey(ExperienceCategory, verbose_name=_("category"), blank=True, null=True,
                                 on_delete=models.SET_NULL)
    is_clinic = models.BooleanField(default=False, verbose_name=_("In Jineart Clinic?"))
    is_lab = models.BooleanField(default=False, verbose_name=_("In Jineart Lab?"))

    class Meta:
        verbose_name = _("Experience Item")
        verbose_name_plural = _("Experience Items")

    def __str__(self):
        return str(self.pk)
