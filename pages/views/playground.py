from django.views.generic.base import TemplateView


class PlaygroundView(TemplateView):
    template_name = "playground.html"