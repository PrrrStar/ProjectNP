from django.shortcuts import render,redirect, get_object_or_404

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate


import re
from django.http import JsonResponse, Http404

from .models import User
from myside.models import Category
from myside.models import Product

from .forms import *

def user_profile(request):
    user        = request.user
    products    = Product.objects.all()
    context     = {
        'user':user,
        'products':products,
    }
    return render(request, 'accounts/profile.html',context)

from django.contrib.auth.decorators import login_required

@login_required
def edit_user_profile(request):
    user = request.user

    if request.method == "POST":
        form        = EditProfileForm(request.POST or request.FILES, instance=request.user)
        if form.is_valid():
            profile                 = form.save(commit=False)
            profile.username        = form.cleaned_data['username']
            profile.email           = form.cleaned_data['email']
            profile.nickname        = form.cleaned_data['nickname']
            profile.profile         = request.FILES.get("profile")
            profile.introduction    = form.cleaned_data['introduction']
            profile.gender          = form.cleaned_data['gender']
            profile.birth           = form.cleaned_data['birth']
            profile.save()
            return redirect('user_profile')
    else:
        form = EditProfileForm(instance=request.user)

    context     = {
        'user':user,
        'form':form,
    }
    return render(request, 'accounts/edit_profile.html',context)

@login_required
def delete_user_profile(request):
    if request.method =="POST":
        request.user.delete()
        return redirect('/')
    return render(request, 'accounts/delete.html')

# 사용자 로그인
def user_login(request):
    if request.is_ajax():
        # 이메일 주소를 입력하지 않은 경우
        if request.POST.get('email')=="":
            return JsonResponse({'noEmail':True})

        # 비밀번호를 입력하지 않은 경우
        elif request.POST.get('password')=="":
            return JsonResponse({'noPassword':True})

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return JsonResponse({'works':True})
        return JsonResponse({'wrongInformation':True})

    return JsonResponse({'notAjax':True})

def user_logout(request):
    if request.is_ajax():
        auth_logout(request)
        return JsonResponse({'works':True})

    return JsonResponse({'notAjax':True})

def user_signup(request):        
    # request 요청이 ajax 요청인 경우 is_ajax() 함수 사용
    if request.is_ajax():
        # POST 방식으로 요청한 경우, 해당 name이 email인 값을 가져오고 싶은 경우, request.POST.get('email') 사용
        # request 보낸 email 이 빈 문자열인 경우
        if request.POST.get('email') == "":
            return JsonResponse({'noEmail':True})            
        elif request.POST.get('nickname') == "":
            return JsonResponse({'noNickname':True})
        # request 요청에서 file type이 있는 경우, 해당 데이터는 request.FILES.get(name)으로 가져온다.                
        
        #elif request.FILES.get('profile', None) is None:
        #    return JsonResponse({'noProfile':True})
        
        elif request.POST.get('password') == "":
            return JsonResponse({'noPassword':True})
        elif request.POST.get('password2') == "":
            return JsonResponse({'noPassword2':True})



        # request로 받은 email 값이 이메일 형식이 아닌 경우
        signup_email = request.POST.get('email')
        if '@' not in signup_email or '.' not in signup_email:
            return JsonResponse({'wrongEmail':True})

        index = signup_email.index('.')
        try:
            signup_email[index + 1]
        except IndexError:
            return JsonResponse({'wrongEmail': True})

        # request로 받은 email 값이 이미 등록된 email인 경우
        if User.objects.filter(email=request.POST.get('email')).exists():
            return JsonResponse({'emailExists':True})

        # request로 받은 nickname 값이 이미 등록된 nickname인 경우
        if User.objects.filter(nickname=request.POST.get('nickname')).exists():
            return JsonResponse({'nicknameExists':True})

        # request로 받은 realName에 영문자, 숫자, 특수문자가 존재하는 경우
        #wrong_str = re.compile('[a-zA-Z0-9-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]')
        #if wrong_str.search(request.POST.get('realName')):
        #    return JsonResponse({'wrongName':True})

        # request로 받은 realName 길이가 5자리를 초과한 경우
        #if len(request.POST.get('realName')) > 5:
        #    return JsonResponse({'tooLongName':True})

        # request로 받은 password가 비밀번호 형식에 적합하지 않은 경우 (8자리이상 & 영어 소문자/대문자/특수문자/숫자 중 3개 이상 조합)
        password = request.POST.get('password')
        if len(password) < 8:
            return JsonResponse({'shortLength':True})
        lower_case = re.compile('[a-z]')
        higher_case = re.compile('[A-Z]')
        number = re.compile('[0-9]')
        symbol = re.compile('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]')

        i = 0
        count = 0
        if re.search(lower_case, password):
            count += 1
        if re.search(higher_case, password):
            count += 1
        if re.search(number, password):
            count += 1
        if re.search(symbol, password):
            count += 1
        # 문자 조합이 3가지 미만일 경우
        if count < 3:
            return JsonResponse({'wrongCombination':True})

        # request로 받은 password2와 password 값이 일치하지 않는 경우
        if request.POST.get('password') != request.POST.get('password2'):
            return JsonResponse({'notMatch':True})


        # 사용자가 작성한 회원가입 내용 형식이 정상인 경우
        email = request.POST.get('email')
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')

        user = User(
            email=email,
            nickname=nickname,
            )
        user.set_password(password)
        user.save()

        return JsonResponse({'works':True})

    return JsonResponse({'notValid':True})
