from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from config.sitemaps import sitemaps

urlpatterns = [
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    path("jet/dashboard/", include("jet.dashboard.urls", namespace="jet-dashboard")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("rosetta/", include("rosetta.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path("", include("page.urls")),
)
