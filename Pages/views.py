from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'Home.html'

#if you dont import the class you want to subclass from it will throw a attribute error cuz you made a 
#custom class with no methods 



