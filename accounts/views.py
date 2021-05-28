from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.views.generic import TemplateView,FormView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from .forms import UsrCreateForm,LoginForm
from .models import User



# Create your views here.

class TopPage(TemplateView):
    template_name = "base.html"

class UserCreateView(FormView):
    form_class = UsrCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:base')


    def form_valid(self,form):
        context = {
            'form':form
        }
        if self.request.POST['next'] == 'back':
            return render(self.request,'accounts/signup.html',context)

        elif self.request.POST['next']  == 'confirm':
            return render(self.request,'accounts/signupconfirm.html',context)
        
        elif self.request.POST['next'] == 'regist':
            form.save()
            user = authenticate(
                email = form.cleaned_data['email'],
                # username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(self.request,user)
            return super.form_valid(form)
        else:
            return redirect(reverse_lazy('base'))

class LoginViews(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:base')

class LogoutViews(LogoutView):
    template_name = 'accounts/logout.html'
    success_url = reverse_lazy('accounts:loggedout')

class LogedoutViews(TemplateView):
    template_name="accounts/logged_out.html"
