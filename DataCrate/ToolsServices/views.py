from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"ToolsServices/ToolsServicesHome.html")

def SpecialLinks(request):
    return render(request,"ToolsServices/SpecialLinks.html")