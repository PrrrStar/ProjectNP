from django.shortcuts import render,redirect
#from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate

#Session Create
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return redirect(request,'/', {'error':'돌아가. 당신은 내편이 아닙니다.'})
    else:
        return redirect(request,'/')

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