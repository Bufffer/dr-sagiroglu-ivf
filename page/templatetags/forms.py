from django import template
from page.forms import HomeContactForm

register = template.Library()


@register.simple_tag
def get_home_contact_form():
    return HomeContactForm()

@register.simple_tag
def get_first_step_form():
    return HomeContactForm()
