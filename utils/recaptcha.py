import requests
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class RecaptchaValidationError(Exception):
    pass


def recaptcha_check(recaptcha_response):
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    value = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    try:
        response = requests.post(verify_url, value)
        response.raise_for_status()
    except requests.HTTPError as exc:
        raise RecaptchaValidationError(_("Recaptcha doğrulaması başarısız! ") + str(exc))
    result = response.json()

    return result['success']


def validate_recaptcha(data):
    if not settings.RECAPTCHA_VALIDATION_ACTIVE:
        return

    recaptcha_response = data.get('g-recaptcha-response')
    recaptcha_response_result = recaptcha_check(recaptcha_response)

    if not recaptcha_response_result:
        raise RecaptchaValidationError(_("Recaptcha doğrulaması başarısız!"))
