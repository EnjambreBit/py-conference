from conferences.models.profiles import Profile
from conferences.models.speakers import Speaker
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView


class CollaboratorsView(TemplateView):
    template_name = "event/collaborators.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = User.objects.filter(groups__name='Colaboradores') \
            .order_by("profile__first_name")
        context["profiles"] = [user.profile for user in queryset]
        context["title"] = "Colaboradores"
        return context


class AcademicCommitteeView(CollaboratorsView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = User.objects.filter(groups__name='Comité académico') \
            .order_by("profile__first_name")
        context["profiles"] = [user.profile for user in queryset]
        context["title"] = "Comité académico"
        return context


class ProceedingsView(CollaboratorsView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = User.objects.filter(groups__name='Actas') \
            .order_by("profile__first_name")
        context["profiles"] = [user.profile for user in queryset]
        context["title"] = "Actas"
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
