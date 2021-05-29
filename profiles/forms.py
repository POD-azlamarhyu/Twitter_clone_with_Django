from django import forms
from .models import Profiles


class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ["account_id","location","bio","icon","header_img"]
        label = {"account_id":"アカウント ID","location":"場所","bio":"自己紹介","icon":"アイコン","header_img":"ヘッダー画像"}


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'