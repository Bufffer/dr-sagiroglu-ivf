from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimestampStarterModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BannerStarterModel(models.Model):
    translations = dict(
        banner_title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Banner Title")),
        banner_description=RichTextField(verbose_name=_("Banner Description"), blank=True, null=True),
    )
    banner_image = models.ImageField(_("Banner Image"), upload_to="banners", blank=True, null=True)
    banner_overlay = models.BooleanField(_("Banner Overlay"), default=False)

    class Meta:
        abstract = True
