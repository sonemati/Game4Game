from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfileInfo


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('location', 'profile_pic')
