from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from page import models
from page.admin import seo_fields
from utils.admin import OneEntityModel


@admin.register(models.HomePageSeo)
class HomePageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Seo Information"), {"fields": seo_fields}),
    )
    filter_vertical = ("meta_keywords",)


@admin.register(models.BannerSlide)
class BannerSlideAdmin(TranslatableAdmin):
    list_display = ("id", "maintitle", "order")
    fields = ("maintitle", "subtitle", "description", "image", "redirect_link", "order")
    list_editable = ("order",)
