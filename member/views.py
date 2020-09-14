from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from django.http import JsonResponse
from .serializers import ProfileSerializer
from django.shortcuts import render, get_object_or_404, redirect
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from .models import *
from .forms import *

# Create your views here.


def signup(request):
    return render(request, 'member/signup.html')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(
                email=email,
                password=password
            )

            if user:
                django_login(request, user)
                return redirect('/')
            login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
    else:
        login_form = LoginForm()
    return render(request, 'member/login.html', {'login_form': login_form})


def profile_detail(request, id):
    profile = get_object_or_404(Profile, id=id)
    return render(request, 'member/detail.html', {'profile': profile})
