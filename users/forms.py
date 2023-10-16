from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image']



