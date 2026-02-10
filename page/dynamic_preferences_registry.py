from django.utils.translation import ugettext_lazy as _
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.types import StringPreference

SECTION_NAME = "page"
page = Section(SECTION_NAME)

saved_preferences = global_preferences_registry.manager()


@global_preferences_registry.register
class PhoneNumber(StringPreference):
    section = page
    name = "phone_number"
    default = "+123 456 7890"
    verbose_name = _("Phone Number")


@global_preferences_registry.register
class EmailAddress(StringPreference):
    section = page
    name = "email_address"
    default = "info@jineart.com"
    verbose_name = _("Email Address")


@global_preferences_registry.register
class Address(StringPreference):
    section = page
    name = "address"
    default = ""
    verbose_name = _("Address")


@global_preferences_registry.register
class AddressMapLink(StringPreference):
    section = page
    name = "address_map_link"
    default = ""
    verbose_name = _("Address Map Link")


@global_preferences_registry.register
class FacebookLink(StringPreference):
    section = page
    name = "facebook_link"
    default = ""
    verbose_name = _("Facebook Link")


@global_preferences_registry.register
class InstagramLink(StringPreference):
    section = page
    name = "instagram_link"
    default = ""
    verbose_name = _("Instagram Link")


@global_preferences_registry.register
class WhatsappLink(StringPreference):
    section = page
    name = "whatsapp_link"
    default = ""
    verbose_name = _("Whatsapp Link")


@global_preferences_registry.register
class YoutubeLink(StringPreference):
    section = page
    name = "youtube_link"
    default = ""
    verbose_name = _("Youtube Link")
