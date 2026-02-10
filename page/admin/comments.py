from django.contrib import admin
from parler.admin import TranslatableAdmin

from page import models


@admin.register(models.PatientComment)
class PatientCommentAdmin(TranslatableAdmin):
    fields = ("name", "role", "comment", "image", "order")
    list_display = ("name", "order")
    list_editable = ("order",)
