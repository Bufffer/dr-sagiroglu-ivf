from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from page import models
from page.admin import seo_fields, banner_fields
from page.admin.faqs import FAQInlineModelAdmin, faqs_fields
from utils.admin import OneEntityModel


@admin.register(models.ServicesPageSeo)
class ServicesPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Banner Information"), {"fields": banner_fields}),
        (_("Seo Information"), {"fields": seo_fields}),
    )
    filter_vertical = ("meta_keywords",)


@admin.register(models.ServiceCategory)
class ServiceCategoryAdmin(TranslatableAdmin):
    fieldsets = (
        (
            _("Content"),
            {"fields": ("title", "slug")},
        ),
    )
    list_display = ("id", "title", "slug")

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)}


@admin.register(models.ServiceItem)
class ServiceItemAdmin(TranslatableAdmin):
    fieldsets = (
        (
            _("Content"),
            {
                "fields": (
                    "category",
                    "title",
                    "slug",
                    "description",
                    "content",
                    "image",
                    "icon",
                    "in_navbar",
                    "in_home",
                    "in_about_page",
                    "in_doctor_page",
                    "order",
                )
            },
        ),
        (_("Banner Information"), {"fields": banner_fields}),
        (_("Seo Information"), {"fields": seo_fields}),
        faqs_fields,
    )
    filter_vertical = ("meta_keywords",)
    list_display = (
        "title",
        "slug",
        "in_navbar",
        "in_home",
        "in_about_page",
        "in_doctor_page",
        "order",
    )
    list_filter = (
        "category",
        "in_navbar",
        "in_home",
        "in_about_page",
        "in_doctor_page",
    )
    list_editable = ("in_navbar", "in_home", "in_about_page", "in_doctor_page", "order")
    inlines = [FAQInlineModelAdmin]

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)}
