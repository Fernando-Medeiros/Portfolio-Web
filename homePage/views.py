from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class HomePage(TemplateView):
    template_name = 'home.html'

class ProfilePage(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'