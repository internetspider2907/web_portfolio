from django import forms
from .models import WorkImage


class WorkImageForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}), required=True)

    class Meta:
        model = WorkImage
        fields = ['title', 'image']
