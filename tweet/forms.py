from django import forms
from .models import *

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','images','videos']

    def clean_content(self):
        text = self.cleaned_data.get("text")
        if len(text) > 500:
            raise forms.ValidationError("文字数をオーバーしています。500文字以下にしてください")

        return text