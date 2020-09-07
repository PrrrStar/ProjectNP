from django import forms
from .models import Profile


class SignupForm(forms.Form):
    first_name = forms.CharField(label=('이름'),
                                 max_length=30,
                                 widget=forms.TextInput())
    last_name = forms.CharField(label=('성'),
                                max_length=30,
                                widget=forms.TextInput())
    phone = forms.CharField(label=('전화번호'),
                            max_length=30,
                            widget=forms.TextInput())

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = Profile()
        profile.user = user
        profile.phone = self.cleaned_data['phone']
        profile.save()
