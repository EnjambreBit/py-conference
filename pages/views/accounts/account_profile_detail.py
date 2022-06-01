from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from conferences.models.profiles import Profile


class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            profile = Profile.objects.get(user=self.request.user)
            context["profile"] = profile
            context["registrations"] = profile.registrations.all()

        except Profile.DoesNotExist:
            context["profile"] = None

        return context
