import os

if not os.path.exists("public/logs"):
    os.makedirs("public/logs")

LOGGING = {
    "version": 1,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        }
    },
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "WARNING",
            "formatter": "verbose",
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "WARNING",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "public/logs/server.log",
            "maxBytes": 1024 * 1024 * 10,
            "backupCount": 2,
            "formatter": "verbose",
        },
    },
    "loggers": {"django": {"handlers": ["console"]}},
    "root": {
        "handlers": ["console", "file"],
        "level": "WARNING",
    },
}
