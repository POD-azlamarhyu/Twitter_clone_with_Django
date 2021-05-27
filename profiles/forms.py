from django import forms
from django.contrib.forms import UserCreationForm
from .models import Profiles

class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ["account_id","location","bio","icon","header_img"]

    def __init__(self,*args,**kwargs):
        kwargs.setdefault('label_suffix','')
        super().__init__(*args,**kwargs)