from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from page import models
from page.admin import seo_fields, banner_fields
from utils.admin import OneEntityModel
from page.admin.faqs import FAQInlineModelAdmin, faqs_fields


@admin.register(models.BlogsPageSeo)
class BlogsPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Banner Information"), {"fields": banner_fields}),
        (_("Seo Information"), {"fields": seo_fields}),
    )
    filter_vertical = ("meta_keywords",)


@admin.register(models.BlogCategory)
class BlogCategoryAdmin(TranslatableAdmin):
    fieldsets = ((_("Content"), {"fields": ("title", "slug")}),)
    list_display = ("id", "title", "slug")

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)}


@admin.register(models.Blog)
class BlogAdmin(TranslatableAdmin):
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
                    "author",
                    "author_image",
                )
            },
        ),
        (_("Banner Information"), {"fields": banner_fields}),
        (_("Seo Information"), {"fields": seo_fields}),
        faqs_fields,
    )
    filter_vertical = ("meta_keywords",)
    list_display = ("title", "slug", "category", "view_count")
    list_filter = ("category",)
    inlines = [FAQInlineModelAdmin]

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)}
