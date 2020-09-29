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
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'name':'username',
            }
        )
    )
    email= forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'name':'email',
            }
        )
    )
    nickname= forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'name':'nickname',
            }
        )
    )
    profile= forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class':'form-control',
                'name':'profile',
            }
        )
    )
    introduction= forms.CharField(
        required=False,
        widget = forms.Textarea(
            attrs={
                'class':'form-control',
                'name':'introduction',
            }
        )
    )
    CHOICES=[('male','Male'),('female','Female'),('other','Other')]
    gender= forms.ChoiceField(
        choices=CHOICES,
        required=False,
        widget = forms.Select(
            attrs={
                'class':'form-control',
                'name':'gender',
            }
            
        )
    )
    birth= forms.DateField(
        required=False,
        widget = forms.DateInput(
            attrs={
                'class':'form-control',
                'name':'birth',
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