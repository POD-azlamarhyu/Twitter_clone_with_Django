from .models import Profiles
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ProfilesForm(forms.ModelForm):

    account_id = forms.CharField(
        initial = '',
        label = 'アカウント ID',
        max_length=255,
        required=True,
    )
    location = forms.CharField(
        initial = '',
        label = '場所',
        max_length=220,
        required=False,
    ) 
    bio = forms.CharField(
        initial = '',
        label = '自己紹介',
        widget=forms.Textarea,
        required = False,
    )
    icon = forms.ImageField(
        initial = '',
        label = 'アイコン',
        required = False,
    )
    header_img = forms.ImageField(
        initial = '',
        label = 'ヘッダーイメージ',
        required = False,
    )
    class Meta:
        model = User
        fields = ["username","email"]


    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'

    def save(self):
        data = self.cleaned_data
        print(data)
        profile = Profiles(
            user = data['user'],
            account_id=data['account_id'],
            location=data['location'],
            bio = data['bio'],
            icon= data['icon'],
            header_img = data['header_img'],
        )

        profile.save()