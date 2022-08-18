import imp
import profile
from django.views.generic import TemplateView
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.http import HttpResponse

from  conferences.models.talks import Talk
from  conferences.models.talk_registration  import TalkRegistration as TR
from conferences.models.profiles import Profile


class TalkRegistration(LoginRequiredMixin, TemplateView):
    template_name = "event/talk-registration.html"
    model = Talk

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["talleres"] = self.get_talleres()
        context["inscripciones"] = self.get_inscripciones()
        return self.render_to_response(context)

    def get_talleres(self) :
        type_talk = Q(talk_type='workshop') | Q(talk_type='sprints')
        qs = Talk.objects.filter(type_talk, event__active=True, status='published')
        return qs

    def get_inscripciones(self) :
        qs = TR.objects.filter(profile__user=self.request.user)
        datos = [ item.talk.id for item in qs]
        return datos

def TalkRegistrationAdd(request, pk):
    try:
        talk = Talk.objects.get(id=pk)
        if talk != None:
            try:
                registro:TR = TR()
                registro.profile = Profile.objects.get(user=request.user)
                registro.talk = talk
                registro.save()
            except registro.DoesNotExist:
                return HttpResponse("Register not found", status=404)
    except Talk.DoesNotExist:
        return HttpResponse("Talk not found", status=404)
    return redirect(request.META['HTTP_REFERER'])

def TalkRegistrationDel(request, pk):
    try:
        talk:Talk = Talk.objects.get(id=pk)
        profile = Profile.objects.get(user=request.user)
        registro:TR = TR.objects.get(talk=talk, profile=profile)
        registro.delete()
    except Talk.DoesNotExist:
        return HttpResponse("Talk not found", status=404)
    except Profile.DoesNotExist:
        return HttpResponse("Profile not found", status=404)
    except registro.DoesNotExist:
        return HttpResponse("Register not found", status=404)
    except :
        return HttpResponse("Error inesperado", status=404)
    

    return redirect(request.META['HTTP_REFERER'])
