from conferences.models.profiles import Profile
from conferences.models.events import Event
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


def EntradaView(request, *args, **kwargs):
        profile:Profile = Profile.objects.get(user= request.user)
        event = Event.objects.filter(active=True).first()

        templete_file = "entrada.html"
        context = {
            "profile": profile,
            "event": event,
            "qr_text":  f"SyPy 2022\n{profile.full_name}\n{profile.email}"
            }
        template_string = render_to_string(templete_file, context)
        html = HTML(string=template_string, base_url=request.build_absolute_uri())
        pdf_file = html.render()
        pdf = pdf_file.write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f"attachment; filename=entrada_sypy2022.pdf"
        
        return response
