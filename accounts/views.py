from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.views.generic import TemplateView
# Create your views here.

class TopPage(TemplateView):
    template_name = "top.html"

class LoginAccount():
    
    def loginView(request,*args,**kwargs):
        form = AuthenticationForm(request,data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("/")

        context = {
            "form":form,
            "btn_label":"ログイン",
            "title":"ログイン"
        }
        return render(request,"accounts/login.html",context)

    def logoutView(request,*args,**kwargs):
        if request.method == "POST":
            logout(request)
            return redirect("/login")

        context={
            "form":None,
            "description":"ログアウトしますか？",
            "btn_label":"Logout",
            "title":"Logout"
        }
        return render(request,"account/login.html",context)

class CreateAccount():
    def registerView(request,*args,**kwargs):
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=True)
            user.set_password(form.cleaned_data.get("password1"))
            login(request,user)
            return redirect("/")

        context={
            "form":form,
            "btn_label":"登録",
            "title":"登録"
        }

        return render(request,"accounts/create.html",context)