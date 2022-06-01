from pages.forms.account_registration import AccountRegistrationForm
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.core.exceptions import ImproperlyConfigured
from conferences.models.profiles import Profile
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class AccountRegistrationView(FormView):
    template_name = "account/account-registration.html"
    form_class = AccountRegistrationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]

        user = User.objects.create_user(username=email, email=email, password=password)
        user.is_superuser = False
        user.is_staff = False
        user.save()

        profile = Profile.objects.create(
            user=user,
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            nickname=form.cleaned_data["nickname"],
            gender=form.cleaned_data["gender"],
            phone=form.cleaned_data["phone"],
        )

        return HttpResponseRedirect(self.get_success_url())
