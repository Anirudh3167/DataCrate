import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def EditorBase(request):
    data = {
        "name" : "", "content" : "", "data" : "10-01-2023",
    }
    return render(request,"Editor/Editor.html", context = data)

def EditorHome(request, link):
    if link is not None:
        # Get the editor content.
        data = {
            "name" : "Some Name",
            "content" : "Hello World",
            "date" : "10-01-2023",
        }
    else:
        data = {
            "name" : "", "content" : "", "data" : "10-01-2023",
        }
    return render(request,"Editor/Editor.html", context = data)

def EditorGenerateLink(request):
    if request.method == 'POST':
        # Copy this to database.
        print(json.load(request))

        return JsonResponse({'code':'123A'})