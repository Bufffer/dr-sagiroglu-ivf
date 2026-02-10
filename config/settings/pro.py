from .base import *

# Railway handles SSL/HTTPS, don't redirect again
SECURE_SSL_REDIRECT = False

# Railway proxy headers
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

X_FRAME_OPTIONS = env("X_FRAME_OPTIONS", default="SAMEORIGIN")

# CSRF and CORS for Railway
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://*.up.railway.app',
]

# Don't apply extra security for now
APPLY_EXTRA_SECURITY = env.bool("APPLY_EXTRA_SECURITY_SETTINGS", default=False)

if APPLY_EXTRA_SECURITY:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 86400
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
