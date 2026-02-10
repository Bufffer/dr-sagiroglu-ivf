from django.views.generic import TemplateView, DetailView

from page import models, forms
from utils.views import CategoriedListView, TranslatableDetailViewMixin, HandleEmailFormView


class HomePage(TemplateView):
    template_name = "page/home.html"


class AboutPage(TemplateView):
    template_name = "page/about/about.html"


class AboutDoctorPage(TemplateView):
    template_name = "page/about/doctor.html"


class WhyUsPage(TemplateView):
    template_name = "page/about/why-us.html"


class SuccessRatesPage(TemplateView):
    template_name = "page/about/success-rates.html"


class HowItWorksPage(TemplateView):
    template_name = "page/about/how_it_works.html"


class ContactPage(TemplateView):
    template_name = "page/contact.html"


class ServicesListView(CategoriedListView):
    template_name = "page/services.html"
    paginate_by = 9
    context_object_name = "services"
    model = models.ServiceItem
    category_model = models.ServiceCategory


class ServicesDetailView(TranslatableDetailViewMixin, DetailView):
    template_name = "page/service-detail.html"
    context_object_name = "service"
    view_url_name = "services_detail"
    model = models.ServiceItem


class JourneyPage(TemplateView):
    template_name = "page/journey.html"
    context_object_name = "journey"
    view_url_name = "journey"
    model = models.JourneyItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.request.GET.get("item")
        if slug:
            context["journey"] = self.model.objects.get(translations__slug=slug)
        else:
            context["journey"] = self.model.objects.first()
        return context


class ExperiencePage(CategoriedListView):
    template_name = "page/experience.html"
    paginate_by = 9
    context_object_name = "experiences"
    model = models.ExperienceItem
    category_model = models.ExperienceCategory


class BlogListView(CategoriedListView):
    template_name = "page/blogs.html"
    paginate_by = 5
    context_object_name = "blog_list"
    model = models.Blog
    category_model = models.BlogCategory

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        author = self.request.GET.get("author")
        if author:
            queryset = queryset.filter(author=author)
        if search:
            queryset = queryset.active_translations(title__icontains=search)
        return queryset


class BlogDetailView(TranslatableDetailViewMixin, DetailView):
    template_name = "page/blog-details.html"
    context_object_name = "blog"
    model = models.Blog
    view_url_name = "blog_detail"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increase_view_count()
        return response


class GDPRPage(TemplateView):
    template_name = "page/gdpr.html"


class PrivacyPage(TemplateView):
    template_name = "page/privacy.html"


class PricingPlanDetailPage(DetailView):
    template_name = "page/pricing-plan.html"
    context_object_name = "plan"
    model = models.PricingPlan


class PricingPage(TemplateView):
    template_name = "page/pricing.html"


class HomeContactFormView(HandleEmailFormView):
    subject = "Jineart IVF - Anasayfa Form Gönderildi!"
    email_template_name = "emails/home_contact_form.html"
    form_identifier = "home-contact-form"
    form_class = forms.HomeContactForm

    def get_email_context(self, data):
        return {
            "full_name": data.get("full_name", ""),
            "email": data.get("email", ""),
            "full_phone_number": data.get("contact-full_number", ""),
            "service": data.get("service", ""),
            "phone": data.get("phone", ""),
            "message": data.get("message", ""),
        }
    
class FirstStepFormView(HandleEmailFormView):
    subject = "Jineart IVF - First Step Form Gönderildi!"
    email_template_name = "emails/first_step_form.html"
    form_identifier = "first-step-form"
    form_class = forms.FirstStepForm
    
    def get_email_context(self, data):
        return {
            "full_name": data.get("full_name", ""),
            "email": data.get("email", ""),
            "full_phone_number": data.get("contact-full_number", ""),
            "service": data.get("service", ""),
            "phone": data.get("phone", ""),
            "message": data.get("message", ""),
        }