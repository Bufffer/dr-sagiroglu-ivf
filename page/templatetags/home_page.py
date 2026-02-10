from django import template
from page.models import HomePageSeo, BannerSlide

register = template.Library()


@register.simple_tag
def get_home_obj():
    return HomePageSeo.objects.first()


@register.simple_tag
def get_banner_slides():
    return BannerSlide.objects.all().order_by("order")
