from django.views.generic.base import TemplateView


class TwitterNewsView(TemplateView):
    template_name = "twitter-news.html"
