from django.http import HttpResponse
from django.template import loader
from conferences.models.static_pages import StaticPage


def render_static_page(request, slug=None):
    template = loader.get_template("static_page.html")
    try:
        page = StaticPage.objects.get(slug=slug)
    except StaticPage.DoesNotExist:
        return HttpResponse("Page not found", status=404)

    print(page.content)

    content = page.content
    title = content.partition("\n")[0]
    title = title.replace("#", "")
    title = title.replace("**", "")

    context = {
        "title": title,
        "rendered_content": page.rendered_content(),
    }
    return HttpResponse(template.render(context, request))
