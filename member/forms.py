from django import forms
from .models import Profile


class SignupForm(forms.Form):
    first_name = forms.CharField(label=('First name'),
                                 max_length=30,
                                 widget=forms.TextInput())
    last_name = forms.CharField(label=('Last name'),
                                max_length=30,
                                widget=forms.TextInput())
    phone = forms.CharField(label=('Phone number'),
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
