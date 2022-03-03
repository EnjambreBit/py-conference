from django.http import HttpResponse
from django.template import loader



def profile_register(request):
    return HttpResponse("register Ok")