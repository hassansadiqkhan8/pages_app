from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "base/home.html"


class AboutPageView(TemplateView):
    template_name = "base/about.html"