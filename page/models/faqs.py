from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


faqs_fields = dict(
    faq_subtitle=models.CharField(
        _("FAQ Subtitle"), max_length=250, blank=True, null=True
    ),
    faq_title=models.CharField(_("FAQ Title"), max_length=250, blank=True, null=True),
    faq_description=models.TextField(_("FAQ Description"), blank=True, null=True),
)


class FAQ(TranslatableModel):
    translations = TranslatedFields(
        question=models.CharField(max_length=250, verbose_name=_("Question")),
        answer=RichTextField(verbose_name=_("Answer")),
    )
    service = models.ForeignKey(
        "page.ServiceItem",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Service"),
    )
    blog = models.ForeignKey(
        "page.Blog",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Blog"),
    )
    about = models.ForeignKey(
        "page.AboutPageSeo",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("About Page"),
    )
    about_doctor = models.ForeignKey(
        "page.AboutDoctorPageSeo",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Cengiz Sagiroglu Page"),
    )
    about_clinic = models.ForeignKey(
        "page.JineartClinicPageSeo",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Jineart Clinic Page"),
    )
    about_lab = models.ForeignKey(
        "page.JineartLabPageSeo",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Jineart Lab Page"),
    )
    howitworks = models.ForeignKey(
        "page.HowItWorksPageSeo",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("How It Works Page"),
    )

    class Meta:
        verbose_name = _("Frequently Asked Question")
        verbose_name_plural = _("Frequently Asked Questions")

    def __str__(self):
        return self.question
