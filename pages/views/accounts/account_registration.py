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
        print("xxx")

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
            document_type=form.cleaned_data["document_type"],
            document_number=form.cleaned_data["document_number"],
            birth_date=form.cleaned_data["birth_date"],
            company=form.cleaned_data["company"],
            job_title=form.cleaned_data["job_title"],
            institution_name=form.cleaned_data["institution_name"],
            study_program=form.cleaned_data["study_program"],
            student_id=form.cleaned_data["student_id"],
        )

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print("xxxx")
        return response
