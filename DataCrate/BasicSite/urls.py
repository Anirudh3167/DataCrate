from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

app_name = "BasicSite"

urlpatterns = [
    # File Sharing
    path('', Home, name = "Home"),
    path('dashboard',Dashboard,name='Dashboard'),
    path('profile',UserProfile,name='Profile'),
    path('sign-in',SignIn,name='SignIn'),
    path('sign-up',SignUp,name='SignUp'),
]
urlpatterns += staticfiles_urlpatterns()