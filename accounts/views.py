from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.views.generic import TemplateView,FormView,UpdateView
from django.urls import reverse_lazy
from .forms import UsrCreateForm
from .models import User


# Create your views here.

class TopPage(TemplateView):
    template_name = "base.html"

class UserCreateView(FormView):
    formClass = UsrCreateForm
    templateName = 'accounts/signup.html'
    successurl = reverse_lazy('accounts:top.html')


    def formValid(self , form):
        context = {
            'form':form
        }
        if self.request.POST['next'] == 'back':
            return render(self.request,'accounts/signup.html',context)

        elif self.request.POST['next']  == "confirm":
            return render(self.request,'accounts/signupconfirm.html',context)
        
        elif self.request.POST['next'] == "regist":
            form.save()
            user = authenticate(
                # email = form.cleaned_data['email'],
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(self.request,user)
            return super.form_valid(form)
        else:
            return redirect(reverse_lazy('top'))