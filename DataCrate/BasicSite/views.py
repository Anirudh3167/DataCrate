from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"BasicSite/HomePage.html")

def UserProfile(request):
    return render(request,'BasicSite/UserProfile.html')

def Dashboard(request):
    return render(request,'BasicSite/dashboard.html')

def SignIn(request):
    return render(request,'BasicSite/SignIn.html')

def SignUp(request):
    return render(request,'BasicSite/SignUp.html')