from .main import LANGUAGES, LANGUAGE_CODE, SITE_ID

PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE

PARLER_LANGUAGES = {
    SITE_ID: tuple({"code": code} for code, name in LANGUAGES),
    "default": {
        "fallbacks": [LANGUAGE_CODE],
        "hide_untranslated": False,
    },
}
