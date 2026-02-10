from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from page import models
from page.admin import seo_fields, banner_fields
from utils.admin import OneEntityModel


@admin.register(models.ExperiencePageSeo)
class ExperiencePageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Banner Information"), {"fields": banner_fields}),
        (_("Seo Information"), {"fields": seo_fields}),
    )
    filter_vertical = ("meta_keywords",)


@admin.register(models.ExperienceCategory)
class ExperienceCategoryAdmin(TranslatableAdmin):
    fields = ("title", "slug")

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)}


@admin.register(models.ExperienceItem)
class ExperienceItemAdmin(admin.ModelAdmin):
    fields = ("image", "category", "is_clinic", "is_lab")
    list_display = ("category", "is_clinic", "is_lab")
    list_filter = ("category", "is_clinic", "is_lab")
    list_editable = ("is_clinic", "is_lab")
