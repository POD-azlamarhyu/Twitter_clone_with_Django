from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserCreationForm
from .models import User


class UsrCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')

    def __init__(self,*args,**kwargs):
        kwargs.setdefault('label_suffix','')
        super().__init__(*args,**kwargs)
