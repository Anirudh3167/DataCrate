from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .models import UserDetails
from django.db.models import Q
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    return render(request,"BasicSite/HomePage.html")

def UserProfile(request):
    return render(request,'BasicSite/UserProfile.html')

def Dashboard(request):
    return render(request,'BasicSite/dashboard.html')

def SignIn(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['pass']
        # rememberMe = request.POST['remember-me']
        
        user = authenticate(request, username = uname, password = password)
        if user is None:
            # New user. Send to Signup
            return render(request,'BasicSite/SignUp.html')

        # if (rememberMe == 'on'):
        #     # Generate the refresh key with longer period
        #     pass
        # print(request.authenticated)
        login(request,user)
        return redirect('BasicSite:Dashboard')
    return render(request,'BasicSite/SignIn.html')

def SignUp(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pass']
        # rememberMe = request.POST['remember-me']

        results = list(set( UserDetails.objects.filter(Q(username = uname) | Q(email=email))))
        if results != []:
            # User already exists
            return redirect('BasicSite:Home')
        else:
            user = UserDetails.objects.create(username = uname, email = email, password = make_password(password))
            user.save()

        # if (rememberMe == 'on'):
        #     # Generate the refresh key with longer period
        #     pass
        
        user = authenticate(request = request, username = uname, password = password)
        print(user)
        if user: login(request,user)
        return redirect('BasicSite:Dashboard')
    return render(request,'BasicSite/SignUp.html')


def Logout(request):
    logout(request)
    return redirect('BasicSite:Home')
    