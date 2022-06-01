from django.template.defaulttags import register
from django.utils.safestring import mark_safe
import markdown


@register.filter
def format_as_md(text):
    return mark_safe(markdown.markdown(text))
