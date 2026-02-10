from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from parler.admin import TranslatableAdmin, TranslatableTabularInline, TranslatableStackedInline
from page.admin import seo_fields, banner_fields
from page import models
from utils.admin import OneEntityModel


class PricingPlanFeatureAdmin(TranslatableTabularInline):
    model = models.PricingPlanFeature
    fields = ("name", "is_checked", "order")
    extra = 1


@admin.register(models.PricingPlan)
class PricingPlanAdmin(TranslatableAdmin):
    fieldsets = (
        (
            _("Content"),
            {"fields": ("name", "order", "is_special", "page_title", "content")},
        ),
        (_("Banner Information"), {"fields": banner_fields}),
        (_("Seo Information"), {"fields": seo_fields}),
    )
    filter_vertical = ("meta_keywords",)
    list_display = ("name", "order", "is_special")
    list_editable = ("order", "is_special")
    list_filter = ("is_special",)
    inlines = (PricingPlanFeatureAdmin,)

@admin.register(models.PriceServiceCategory)
class PriceServiceCategoryAdmin(TranslatableAdmin):
    model = models.PriceServiceCategory
    fields = ("title", "slug", "description", "order")
    list_display = ("title", "slug", "order")
    list_editable = ("order",)

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)}

class PriceServiceItemInlineAdmin(TranslatableStackedInline):
    model = models.PriceServiceItem
    fields = ("title", "content", "price", "category", "order")
    extra = 1


@admin.register(models.PricesPageSeo)
class PricesPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Content"), {"fields": ("title", "content")}),
        (_("Banner Information"), {"fields": banner_fields}),
        (_("Seo Information"), {"fields": seo_fields}),
    )
    filter_vertical = ("meta_keywords",)
    inlines = (PriceServiceItemInlineAdmin,)
