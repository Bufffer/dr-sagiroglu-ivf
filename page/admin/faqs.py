from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableStackedInline

from page import models


class FAQInlineModelAdmin(TranslatableStackedInline):
    model = models.FAQ
    fields = ("question", "answer")


faqs_fields = (
    _("FAQ Section"),
    {"fields": ("faq_subtitle", "faq_title", "faq_description")},
)
