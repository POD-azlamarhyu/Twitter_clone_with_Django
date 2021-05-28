from django import forms
from .models import Profiles
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    pass

class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ["account_id","location","bio","icon","header_img"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'