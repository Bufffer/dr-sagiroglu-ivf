from django.urls import path
from django.utils.translation import ugettext_lazy as _

from page import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path(_("about/"), views.AboutPage.as_view(), name="about"),
    path(_("about-doctor/"), views.AboutDoctorPage.as_view(), name="about_doctor"),
    path(_("why-us/"), views.WhyUsPage.as_view(), name="why_us"),
    path(_("success-rates/"), views.SuccessRatesPage.as_view(), name="success_rates"),
    path(_("how-it-works/"), views.HowItWorksPage.as_view(), name="how_it_works"),
    path(_("services/"), views.ServicesListView.as_view(), name="services"),
    path(_("services/<slug>/"), views.ServicesDetailView.as_view(), name="services_detail"),
    path(_("journey/"), views.JourneyPage.as_view(), name="journey"),
    path(_("experience/"), views.ExperiencePage.as_view(), name="experience"),
    path(_("blog/"), views.BlogListView.as_view(), name="blog_list"),
    path(_("blog/<slug>/"), views.BlogDetailView.as_view(), name="blog_detail"),
    path(_("contact/"), views.ContactPage.as_view(), name="contact"),
    path(_("gdpr/"), views.GDPRPage.as_view(), name="gdpr"),
    path(_("privacy/"), views.PrivacyPage.as_view(), name="privacy"),
    path(_("plan/<pk>/"), views.PricingPlanDetailPage.as_view(), name="pricing_plan"),
    path(_("pricing/"), views.PricingPage.as_view(), name="pricing"),
    path(
        "handle-contact-form/",
        views.HomeContactFormView.as_view(),
        name="handle_home_contact_form",
    ),
    path(
        "handle-first-step-form/",
        views.FirstStepFormView.as_view(),
        name="handle_first_step_form",
    ),
]
