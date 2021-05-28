from django.shortcuts import render,redirect,resolve_url,get_object_or_404
from .forms import ProfilesForm
# from django.contrib.auth.forms import UserCreateForm
from django.http import Http404
from django.contrib.auth import get_user_model
from django.views.generic import CreateView,FormView,UpdateView,TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Profiles
from .forms import UserCreateForm,ProfilesForm
# from ..accounts.forms import UsrCreateForm

User = get_user_model()

def profileEditView(request,*args,**kwargs):
    if not request.user.is_authenticated:
        return render(request,"profiles/profile.html")
    
    userForm = UserCreateForm(request.POST or None)
    profileForm = ProfilesForm(request.POST or None)

    if request.method == "POST" and userForm.is_valid() and profileForm.is_valid():
        user = userForm.save(commit=False)
        user.is_active = True
        user.save()

        profile = profileForm.save(commit=False)
        profile.user_id = request.user.user_id
        profile.save()

        return redirect("profiles:profile_detail")

    context = {
        "userFrom":userForm,
        "profileForm":profileForm,
    }

    
    return render(request,"profiles/profileedit.html",context)



# # Create your views here.
# class OnlyYouMixin(UserPassesTestMixin):
#     raise_exception = True
#     def test_func(self):
#         user= self.request.user
#         return user.pk == self.kwargs['pk'] or user.is_superuser

# class ProfilesEditView(OnlyYouMixin,FormView):
#     model = Profiles
#     template_name = 'profiles/profileedit.html'
#     form_class = ProfilesForm
#     #success_url = reverse_lazy('profiles:profiles_detail')

#     def get_success_url(self):
#         return resolve_url('profiles:profile_detail',pk=self.kwargs['pk'])

#     def form_valid(self,form):
        
#         return super().form_valid(form)

#     # def get_form_kwargs(self):
#     #     kwargs = super().get_form_kwargs()
#     #     kwargs.update({
#     #         'account_id' : self.request.profiles.account_id,
#     #         'location' : self.request.profiles.location,
#     #         'bio':self.request.profiles.bio,
#     #         'icon':self.request.profiles.icon,
#     #         'header_img':self.request.profiles.header_img,
#     #     })

#     #     return kwargs
def profileView(request,user_id,*args,**kwargs):
    qs = Profiles.objects.filter(user__user_id=user_id)

    profile = qs.first()
    if not qs.exists():
        raise Http404
    
    if request.user.is_authenticated:
        user = request.user

    context = {
        "user_id":user_id,
        "profile":profile,
    }

    return render(request,"profiles/profile.html",context)

    # def get_queryset(self):
    #     return Profiles.objects.get(id=self.request.profiles.id)