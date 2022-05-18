from django.views.generic.base import TemplateView


class NotImplementedView(TemplateView):
    template_name = "not-implemented.html"
