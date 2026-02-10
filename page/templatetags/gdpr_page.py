from django import template
from page.models import GDPRPageSeo, PrivacyPageSeo

register = template.Library()


@register.simple_tag
def get_gdpr_obj():
    return GDPRPageSeo.objects.first()


@register.simple_tag
def get_privacy_obj():
    return PrivacyPageSeo.objects.first()
