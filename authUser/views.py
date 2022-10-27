from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView



class Profile(TemplateView):
    template_name = 'profile.html'