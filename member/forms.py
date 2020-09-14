from django import forms
from .models import Profile


class SignupForm(forms.Form):
    YEARS = [x for x in range(1920, 2021)]

    first_name = forms.CharField(label=('이름'),
                                 max_length=30,
                                 widget=forms.TextInput())
    last_name = forms.CharField(label=('성'),
                                max_length=30,
                                widget=forms.TextInput())
    nickname = forms.CharField(label=('별명'),
                               max_length=30,
                               widget=forms.TextInput())
    birth = forms.DateField(label=('생년월일'), initial="2000-01-01",
                            widget=forms.SelectDateWidget(years=YEARS))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = Profile()
        profile.user = user
        profile.nickname = self.cleaned_data['nickname']
        profile.birth = self.cleaned_data['birth']
        profile.save()


class LoginForm(forms.Form):
    email = forms.EmailField(label=('이메일'),
                             widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    )
    )
    password = forms.CharField(label=('비밀번호'),
                               widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    )
    )
