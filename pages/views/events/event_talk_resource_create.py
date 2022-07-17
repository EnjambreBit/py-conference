from django.urls import reverse_lazy
from django.views.generic import FormView
from pages.forms.resources import ResourceCreateForm
from conferences.models.talks import Talk
from django.http import HttpResponseRedirect


class TalkResourceCreateView(FormView):
    template_name = "event/event-talk-resource-create.html"
    form_class = ResourceCreateForm

    def get(self, request, pk, *args, **kwargs):
        context_data = self.get_context_data()
        talk = Talk.objects.get(pk=pk)
        context_data["talk"] = talk
        return self.render_to_response(context_data)

    def form_valid(self, form):
        resource_type = form.cleaned_data["resource_type"]
        return HttpResponseRedirect(
            reverse_lazy("talk_resource_create", kwargs={
                "pk": self.kwargs.get("pk"), 
                "type":resource_type 
            }))


