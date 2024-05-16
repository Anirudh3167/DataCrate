from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

app_name = "Editor"

urlpatterns = [
    # File Sharing
    path('', EditorBase, name = "Editor"),
    path('<str:link>', EditorHome, name = "Editor"),
    path('api/editor-generate-link',EditorGenerateLink, name='EditorGenerateLink'),
]
urlpatterns += staticfiles_urlpatterns()