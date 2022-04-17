import mimetypes
import os
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.templatetags.static import static
from .models import Projects
from .forms import ReceivedMessagesForm, ReceivedMessagesSpanishForm
# Create your views here.

class MainPageView(View):
    def get(self, request):
        language = request.GET.get('lan') if request.GET.get('lan') else 'es'
        if language == 'es':
            context = {
                'projects': Projects.objects.all(),
                'contact_form': ReceivedMessagesSpanishForm()
            }
            return render(request, 'main_page/main_page_spanish.html', context)
        else:
            context = {
                'projects': Projects.objects.all(),
                'contact_form': ReceivedMessagesForm()
            }
            return render(request, 'index.html', context)
    
    def post(self, request):
        language = request.GET.get('lan') if request.GET.get('lan') else 'en'
        if language == 'es':
            form = ReceivedMessagesSpanishForm(request.POST)
        else:
            form = ReceivedMessagesForm(request.POST)
        if form.is_valid():
            form.save()
            if language == 'es':
                form = ReceivedMessagesSpanishForm()
            else:
                form = ReceivedMessagesForm()
            response_data = {
                'result': 'success',
                'form_html': render_to_string('main_page/includes/contact_form.html', {'form': form, 'lan': language})
            }
            return JsonResponse(response_data)
        response_data = {
            'error': 'error',
            'message': 'Form invalid',
            'form_html': render_to_string('main_page/includes/contact_form.html', {'form': form})
        }
        response = JsonResponse(response_data)
        response.status_code = 403 # The message couln't be published and return error to ajax code with form data
        print(response)
        return response


def download_cv(request):
    language = request.GET.get('lan')
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'CV-Gregori-Azuaje-Cabanerio-english.pdf' if language == 'en' else 'CV-Gregori-Azuaje-Cabanerio-spanish.pdf'
    filepath = BASE_DIR + '/static/' + filename
    print(BASE_DIR)
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    print(mime_type)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response