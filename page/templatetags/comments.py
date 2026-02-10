from django import template
from page.models import PatientComment

register = template.Library()


@register.simple_tag
def get_patient_comments(limit=None):
    query = PatientComment.objects.all()
    if limit:
        query = query[:limit]
    return query
