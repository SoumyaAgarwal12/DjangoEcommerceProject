# from crypt import methods
from inspect import Parameter
from django.http import HttpResponse
from django.shortcuts import render, redirect
# For Login
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User

from django.conf import settings



def index(request):
    param = {"myEnv" : settings.PROD_ENV}
    return render(request, "index.html", param)

def loginPage(request):
    return HttpResponse("HELLO LOGINPAGE")

def handleLogin(request):
        if request.method == 'POST':
            loginUsername = request.POST['loginUsername']
            loginPassword = request.POST['loginPassword']

            user = authenticate(username = loginUsername, password = loginPassword)
            if user is not None:
                login(request, user)
                # return HttpResponse("HELLO LOGIN")
                return redirect('index')
            else:
                return HttpResponse("Invalid LOGIN")
                # return redirect('index')
        else :
            return HttpResponse("404-Page not found")

def handleLogout(request):
    logout(request)
    # return HttpResponse("Successfull Logout")
    return redirect('index')


        
def ifLogin(request):
    if request.user.is_authenticated:
        print("YES")
        return HttpResponse("CNGOO LOGIN")
    else:
        print("NO")
        return HttpResponse("BYE BYE")
