from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _tr
from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import switch_language

from page.models import seo_translations, SEOStarterModel
from page.models.faqs import faqs_fields
from utils.models import TimestampStarterModel, BannerStarterModel


class BlogsPageSeo(TranslatableModel, SEOStarterModel, BannerStarterModel):
    translations = TranslatedFields(
        **BannerStarterModel.translations, **seo_translations
    )

    class Meta:
        verbose_name = _("Blogs Page SEO")
        verbose_name_plural = _("Blogs Page SEO")

    def __str__(self):
        return _tr("Blogs Page Seo")


class BlogCategory(TranslatableModel, TimestampStarterModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=100),
        slug=models.SlugField(_("Slug"), max_length=100),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")

    def get_absolute_url(self):
        with switch_language(self):
            return "{}?category={}".format(reverse(f"blog_list"), self.slug)

    @property
    def blog_count(self):
        return self.blog_set.count()


class Blog(
    TranslatableModel, SEOStarterModel, TimestampStarterModel, BannerStarterModel
):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200),
        slug=models.SlugField(_("Slug"), max_length=200),
        description=RichTextField(verbose_name=_("Description"), blank=True, null=True),
        content=RichTextUploadingField(_("Content"), blank=True, null=True),
        **BannerStarterModel.translations,
        **seo_translations,
        **faqs_fields,
    )
    category = models.ForeignKey(
        BlogCategory,
        verbose_name=_("Category"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    image = models.ImageField(_("Blog Image"), upload_to="blogs", blank=True, null=True)
    author_image = models.ImageField(
        _("Author Image"), upload_to="blogs/authors", blank=True, null=True
    )
    author = models.CharField(
        verbose_name=_("Author"), max_length=100, blank=True, null=True
    )
    view_count = models.IntegerField(default=0, verbose_name=_("View Count"))

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        with switch_language(self):
            return reverse(f"blog_detail", args=(self.slug,))

    def increase_view_count(self):
        self.view_count += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.banner_title:
            self.banner_title = self.title
        if not self.banner_description:
            self.banner_description = self.description
        if not self.seo_title:
            self.seo_title = self.title
        super().save(*args, **kwargs)
