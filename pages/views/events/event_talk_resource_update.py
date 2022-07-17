from django.views.generic import UpdateView
from django.urls import reverse_lazy
from conferences.models.resources import Resource
from pages.forms.resources import ResourceLinkForm, ResourceFileForm, ResourceImageForm
from django import forms


class EventTalkResourceUpdateView(UpdateView):
    template_name = "event/event-talk-resource-form.html"
    model = Resource

    # # def get(self, request, pk, *args, **kwargs):
    # #     context_data = self.get_context_data()
    # #     talk = Talk.objects.get(pk=pk)
    # #     context_data["talk"] = talk

    def get_form_class(self):
        resource = self.get_object()
        forms_class = {
            "ResourceLink": ResourceLinkForm,
            "ResourceFile": ResourceFileForm,
            "ResourceImage": ResourceImageForm
        }
        return forms_class.get(resource.type, ResourceLinkForm)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["talk"].widget = forms.HiddenInput()
        return form

    # # def get_object(self, queryset=None):
    # #     pk = self.kwargs.get("pk")
    # #     resource = Resource.objects.get(id=pk)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["talk"] = self.get_object().talk
        return context_data

    def get_success_url(self):
        return reverse_lazy("talk_preview", kwargs={ "pk": self.model.talk.id })