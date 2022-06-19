from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import loader
from conferences.models.events import Event
from conferences.models.sponsors import Sponsor
from conferences.models.sponsor_levels import SponsorLevel


class SponsorListView(TemplateView):
    template_name = "sponsor/sponsor-list.html"
    model = Sponsor

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["sponsors_level"] = self.get_sponsors_groups_by_level()
        context["not_sponsors"] = Sponsor.objects.filter(published=True).count() == 0
        return self.render_to_response(context)

    def get_sponsors_groups_by_level(self):
        sponsors_groups_by_level = []
        for sponsor_level in SponsorLevel.objects.all().order_by("-priority"):
            queryset = Sponsor.objects.filter(
                sponsor_level=sponsor_level, published=True
            )
            if queryset.count() > 0:
                sponsors_groups_by_level.append(
                    {"detail": sponsor_level, "sponsors": queryset}
                )
        return sponsors_groups_by_level
