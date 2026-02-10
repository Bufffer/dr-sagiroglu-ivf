from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class PatientComment(TranslatableModel):
    name = models.CharField(_("Name"), max_length=200)
    translations = TranslatedFields(
        role=models.CharField(_("Role"), max_length=200, blank=True, null=True),
        comment=models.TextField(_("Comment"), blank=True, null=True),
    )
    order = models.IntegerField(_("Ordering"), default=0)
    image = models.ImageField(
        _("Image"), upload_to="patient-comments/", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Patient Comment")
        verbose_name_plural = _("Patient Comments")
        ordering = ("order",)
