from django.contrib import admin
from parler.admin import TranslatableAdmin

from page.models import Keywords, seo_translations

admin.site.register(Keywords, TranslatableAdmin)

seo_fields = tuple(seo_translations.keys()) + ("meta_keywords",)

banner_fields = ("banner_title", "banner_description", "banner_image", "banner_overlay")
