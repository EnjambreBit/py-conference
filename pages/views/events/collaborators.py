from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic import DetailView
from conferences.models.speakers import Speaker
from conferences.models.profiles import Profile
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class CollaboratorsView(TemplateView):
    template_name = "event/collaborators.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = User.objects.filter(groups__name='Colaboradores') \
            .order_by("profile__first_name")
        context["profiles"] = [user.profile for user in queryset]
        return context



class CollaboratorDetailView(DetailView):
    model = Profile
    template_name = "event/collaborator-profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()

        if Speaker.objects.filter(profile=profile).count() == 0:
            Speaker.objects.create(
                profile=profile,
                biography=""
            )
        return context

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        self.object = profile

        if profile.user.groups.filter(name="Colaboradores").count() == 0:
            return HttpResponseRedirect(reverse_lazy("collaborators"))

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
