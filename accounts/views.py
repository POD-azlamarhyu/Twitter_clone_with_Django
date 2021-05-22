from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.views.generic import TemplateView
# Create your views here.

class TopPage(TemplateView):
    template_name = "base.html"
