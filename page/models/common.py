from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Keywords(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Keyword"), max_length=100)
    )

    class Meta:
        verbose_name = _("Keyword")
        verbose_name_plural = _("Keywords")

    def __str__(self):
        return self.name


seo_translations = dict(
    seo_title=models.CharField(_("SEO Title"), max_length=200, blank=True, null=True),
    meta_description=models.TextField(_("Meta Description"), blank=True, null=True),
)


class SEOStarterModel(models.Model):
    meta_keywords = models.ManyToManyField(
        Keywords, verbose_name=_("Meta Keywords"), blank=True
    )

    class Meta:
        abstract = True
