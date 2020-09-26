from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

'''class SignupForm(UserCreationForm):
    email = forms.EmailField(
        requried=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'EMAIL',
                'required': 'True',
            }
        )
    )
    class Meta:
        model = User
        fields = {
            'email',
            'nickname',
            'profile',
            'introduction',
            'gender',
            'birth',
        }
'''
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = {
            'email',
            'nickname',
            'profile',
            'introduction',
            'gender',
            'birth',
        }