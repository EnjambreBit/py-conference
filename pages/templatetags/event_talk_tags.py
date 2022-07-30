from django import template

register = template.Library()


@register.inclusion_tag("tags/talk-preview.html")
def talk_preview(talk):
    return {"talk": talk}
