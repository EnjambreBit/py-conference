from re import M
from django.urls import reverse_lazy
from django.views.generic import CreateView
from pages.forms.resources import ResourceLinkForm, ResourceFileForm, ResourceImageForm
from conferences.models.resources import Resource
from conferences.models.talks import Talk
from django import forms
from django.http import HttpResponseRedirect


class TalkResourceCreateByTypeView(CreateView):
    template_name = "event/event-talk-resource-form.html"
    model = Resource

    def get_form_class(self):
        forms = {
            "link": ResourceLinkForm,
            "file": ResourceFileForm,
            "image": ResourceImageForm
        }
        return forms[self.kwargs.get("type", ResourceLinkForm)]

        

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["talk"].widget = forms.HiddenInput()
        return form

    def get_initial(self):
        initial = super().get_initial()
        initial["talk"] = self.kwargs["pk"]
        return initial

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        types = {
            "link": "Link",
            "file": "Archivo",
            "image": "Imagen"
        }
        
        context_data["resource_type"] = types.get(self.kwargs["type"], "Link")
        context_data["talk"] = Talk.objects.get(id=self.kwargs["pk"])
        return context_data

    def form_valid(self, form):
        self.model = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("talk_preview", kwargs={ "pk": self.model.talk.id })