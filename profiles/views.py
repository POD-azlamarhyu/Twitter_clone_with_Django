from django.shortcuts import render,redirect,resolve_url,get_object_or_404
from .forms import ProfilesForm
# from django.contrib.auth.forms import UserCreateForm
from django.http import Http404
from django.contrib.auth import get_user_model
from django.views.generic import CreateView,FormView,UpdateView,TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Profiles
from .forms import ProfilesForm
from django.contrib import messages
# from ..accounts.forms import UsrCreateForm

User = get_user_model()

class ProfileCreateView(LoginRequiredMixin,CreateView):
    model = Profiles
    form_class = ProfilesForm
    template_name = "profiles/profileedit.html"
    success_url = "/"

    def form_valid(self,form):
        messages.success(self.request,"保存しました")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.warning(self.request,"保存できませんでした")
        return super().form_invalid(form)

    # def get_success_url(self):
    #     return resolve_url('edit',pk=self.kwargs['pk'])

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = "profiles/profile.html"
    user_id = User.objects.filter
    
    def get_queryset(self):
        return Profiles.objects.filter(user=self.request.user)

