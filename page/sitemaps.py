from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from utils.sitemaps import ModelSitemap
from page.models import ServiceItem, Blog


class PageStaticViewSitemap(Sitemap):
    i18n = True
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return [
            "home",
            "about",
            "about_doctor",
            "why_us",
            "success_rates",
            "how_it_works",
            "services",
            "journey",
            "experience",
            "blog_list",
            "contact",
            "gdpr",
            "privacy",
        ]

    def location(self, item):
        return reverse(item)


class ServiceSitemap(ModelSitemap):
    model = ServiceItem
    changefreq = "daily"
    priority = 0.7


class BlogSitemap(ModelSitemap):
    model = Blog
    changefreq = "daily"
    priority = 0.7
