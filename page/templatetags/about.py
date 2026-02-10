from django import template

from page.models import AboutPageSeo, AboutDoctorPageSeo, JineartClinicPageSeo, JineartLabPageSeo, HowItWorksPageSeo

register = template.Library()


@register.simple_tag
def get_about_seo_obj():
    return AboutPageSeo.objects.first()


@register.simple_tag
def get_about_doctor_seo_obj():
    return AboutDoctorPageSeo.objects.first()


@register.simple_tag
def get_why_us_seo_obj():
    # WhyUsPageSeo
    return JineartClinicPageSeo.objects.first()


@register.simple_tag
def get_success_rates_seo_obj():
    # SuccessRatesPageSeo
    return JineartLabPageSeo.objects.first()


@register.simple_tag
def get_howitworks_seo_obj():
    return HowItWorksPageSeo.objects.first()
