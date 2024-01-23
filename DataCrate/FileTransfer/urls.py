from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

app_name = "FileShare"

urlpatterns = [
    # File Sharing
    path('', FileShare, name = "FileShare"),
]
urlpatterns += staticfiles_urlpatterns()