from django.shortcuts import render,redirect
#from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


#Session Create
def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
        return redirect('/')
    
    else:
        login_form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'login_form' : login_form})

def logout(request):
    auth_logout(request)
    return redirect('/')


def signup(request):
    #redirect_to = request.REQUEST.get('next','')
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
        #return HttpResponseRedirect(redirect_to)
        return redirect('/')
    else:
        signup_form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'signup_form':signup_form})