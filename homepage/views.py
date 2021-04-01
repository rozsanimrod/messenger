from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'homepage/home.html'





