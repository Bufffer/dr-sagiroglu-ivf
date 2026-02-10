from django import template
from page.models import (
    PricingPlan,
    PricesPageSeo,
    PriceServiceItem,
    PriceServiceCategory,
)

register = template.Library()


@register.simple_tag
def get_pricing():
    query = PricingPlan.objects.all()
    return query


@register.simple_tag
def get_prices_page_obj():
    return PricesPageSeo.objects.first()


@register.simple_tag
def get_prices_items():
    return PriceServiceItem.objects.all()


@register.simple_tag
def get_prices_categories():
    return PriceServiceCategory.objects.all()
