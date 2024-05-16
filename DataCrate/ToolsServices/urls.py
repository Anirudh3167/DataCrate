from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

app_name = "ToolsServices"

urlpatterns = [
    # File Sharing
    path('', Home, name = "Home"),
    path('special-links',SpecialLinksTool,name="SpecialLinks"),
    path('special-links/<str:linkId>',SpecialLinkPage,name="SpecialLinkPage"),
    
]
urlpatterns += staticfiles_urlpatterns()