from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from page import models
from page.admin import seo_fields, banner_fields
from utils.admin import OneEntityModel


@admin.register(models.JourneyPageSeo)
class JourneyPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Banner Information"), {"fields": banner_fields}),
        (_("Seo Information"), {"fields": seo_fields}),
    )
    filter_vertical = ("meta_keywords",)


@admin.register(models.JourneyItem)
class JourneyItemAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Content"), {"fields": ("title", "slug", "content", "description", "image")},),
    )
    list_display = ("id", "title", "slug")

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)}
