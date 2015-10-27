from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class MessageCreateView(CreateView):
    model = Message
    template_name = "message/message_form.html"
    fields = ['name','email', 'title', 'description']
    success_url = reverse_lazy('success')

class Success(TemplateView):
    template_name = "success.html"

class AboutCreateView(CreateView):
    model = About
    template_name = "about/about_form.html"
    fields = ['title']