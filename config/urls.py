from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from config.sitemaps import sitemaps
from django.views.static import serve
from django.views.generic import RedirectView

urlpatterns = [
    # Redirect root to English homepage
    path('', RedirectView.as_view(url='/en/', permanent=False)),
    
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    path("jet/dashboard/", include("jet.dashboard.urls", namespace="jet-dashboard")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("rosetta/", include("rosetta.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
]

# Static files (works in both DEBUG True/False)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Media files - serve in production too (Railway doesn't have Nginx)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Extra media serving for production (Railway)
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns += i18n_patterns(
    path("", include("page.urls")),
    prefix_default_language=True  # Always use /en/ for English (default language)
)
