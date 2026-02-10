from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class HomeContactForm(forms.Form):
    full_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=200)
    full_phone_number = forms.CharField(max_length=200, required=False)
    service = forms.CharField(max_length=200, required=False)
    message = forms.CharField(max_length=200, required=False, widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV3(action="home_contact_form"))


class FirstStepForm(forms.Form):
    full_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=200)
    full_phone_number = forms.CharField(max_length=200, required=False)
    service = forms.CharField(max_length=200, required=False)
    message = forms.CharField(max_length=200, required=False, widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV3(action="first_step_form"))
