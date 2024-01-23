from django.shortcuts import render

# Create your views here.
def EditorHome(request):
    return render(request,"Editor/Editor.html")