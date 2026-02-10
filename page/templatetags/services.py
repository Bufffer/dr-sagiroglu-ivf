from django import template

from page.models import ServicesPageSeo, ServiceItem, ServiceCategory

register = template.Library()


@register.simple_tag
def get_services_seo_obj():
    return ServicesPageSeo.objects.first()


@register.simple_tag
def get_service_categories(limit=None):
    query = ServiceCategory.objects.all()
    if limit:
        return query[:limit]
    return query


@register.simple_tag
def get_services(
    in_home=False,
    in_navbar=False,
    in_about=False,
    in_doctor=False,
    exclude=None,
    limit=None,
):
    query = ServiceItem.objects.all()
    if in_home:
        query = query.filter(in_home=True)
    if in_navbar:
        query = query.filter(in_navbar=True)
    if in_about:
        query = query.filter(in_about_page=True)
    if in_doctor:
        query = query.filter(in_doctor_page=True)
    if exclude:
        query = query.exclude(id=exclude)
    if limit:
        return query[:limit]
    return query
