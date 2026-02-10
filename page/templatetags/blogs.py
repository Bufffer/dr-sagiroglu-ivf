from django import template

from page.models import BlogsPageSeo, Blog, BlogCategory

register = template.Library()


@register.simple_tag
def get_blogs_seo_obj():
    return BlogsPageSeo.objects.first()


@register.simple_tag
def get_blog_categories(limit=None):
    query = BlogCategory.objects.all()
    if limit:
        return query[:limit]
    return query


@register.simple_tag
def get_blogs(category=None, blog=None, limit=None, popular=False, recent=False):
    query = Blog.objects.all()
    if category:
        query = query.filter(category=category)
    if blog:
        query = query.exclude(id=blog.id)
    if popular:
        query = query.order_by('-view_count')
    if recent:
        query = query.order_by('-created_date')
    if limit:
        return query[:limit]
    return query
