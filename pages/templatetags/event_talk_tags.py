from django import template

register = template.Library()



@register.inclusion_tag("tags/talk-preview.html")
def talk_preview(talk, hidden_resources=False):
    context = {
        "talk": talk, 
        "have_resources": False
    }
    if not hidden_resources:
        context["resources"] = talk.resources.all()
        context["have_resources"] = talk.resources.all().count() > 0

    return context


