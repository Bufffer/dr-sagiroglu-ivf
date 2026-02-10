from django import template

from page.models import JourneyPageSeo, JourneyItem

register = template.Library()


@register.simple_tag
def get_journey_seo_obj():
    return JourneyPageSeo.objects.first()


@register.simple_tag
def get_journey_items():
    query = JourneyItem.objects.all()
    return query
