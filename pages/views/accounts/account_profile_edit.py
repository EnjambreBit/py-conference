from django.views.generic import UpdateView
from django.urls import reverse_lazy
from conferences.models.profiles import Profile
from pages.forms.profile import ProfileForm


class ProfileUpdateView(UpdateView):
    template_name = "account/account_profile_edit.html"
    model = Profile
    form_class = ProfileForm

    def get_object(self, queryset=None):
        user = self.request.user
        profile = user.profile
        if profile is None:
            profile = Profile.objects.crete(user=user)
        return profile

    def get_success_url(self):
        return reverse_lazy("profile")