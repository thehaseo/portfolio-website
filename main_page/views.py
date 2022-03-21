from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Projects
from .forms import ReceivedMessagesForm, ReceivedMessagesSpanishForm
# Create your views here.

def redirect_main_english(request):
    return redirect('main_page:main_page_view', 'en')


class MainPageView(View):
    def get(self, request, language):
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
    
    def post(self, request, language):
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
