from django import template

from page.models import ExperiencePageSeo, ExperienceItem, ExperienceCategory

register = template.Library()


@register.simple_tag
def get_experience_seo_obj():
    return ExperiencePageSeo.objects.first()


@register.simple_tag
def get_experience_categories(limit=None):
    query = ExperienceCategory.objects.all()
    if limit:
        query = query[:limit]
    return query


@register.simple_tag
def get_experience_items(category=None, limit=None, clinic=False, lab=False):
    query = ExperienceItem.objects.all()
    if category:
        query = query.filter(category=category)
    if clinic:
        query = query.filter(is_clinic=True)
    if lab:
        query = query.filter(is_lab=True)
    if limit:
        query = query[:limit]
    return query
