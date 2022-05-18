from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin


from conferences.models.profiles import Profile


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["profile"] = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            context["profile"] = None
        
        return context
