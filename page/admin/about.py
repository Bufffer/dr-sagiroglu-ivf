from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from page import models
from page.admin import seo_fields, banner_fields
from utils.admin import OneEntityModel
from page.admin.faqs import FAQInlineModelAdmin, faqs_fields


class AboutPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Content"), {"fields": ("subtitle", "title", "content", "youtube_link", "image")}),
        (_("Banner Information"), {"fields": banner_fields}),
        (_("Seo Information"), {"fields": seo_fields}),
        faqs_fields,
    )
    filter_vertical = ("meta_keywords",)
    inlines = [FAQInlineModelAdmin]


admin.site.register(models.AboutPageSeo, AboutPageSeoAdmin)
admin.site.register(models.AboutDoctorPageSeo, AboutPageSeoAdmin)
admin.site.register(models.JineartClinicPageSeo, AboutPageSeoAdmin)
admin.site.register(models.JineartLabPageSeo, AboutPageSeoAdmin)


@admin.register(models.HowItWorksPageSeo)
class HowItWorksPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = [
        (
            _("Content"),
            {
                "fields": [
                    "subtitle1",
                    "title1",
                    "content1",
                    "image1",
                    "subtitle2",
                    "title2",
                    "content2",
                    "image2",
                    "subtitle3",
                    "title3",
                    "content3",
                    "image3",
                ],
            },
        ),
        (_("Banner Information"), {"fields": banner_fields}),
        (_("Seo Information"), {"fields": seo_fields}),
        faqs_fields,
    ]
    inlines = [FAQInlineModelAdmin]