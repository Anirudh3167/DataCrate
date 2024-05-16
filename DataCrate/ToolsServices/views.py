from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"ToolsServices/ToolsServicesHome.html")

def SpecialLinksTool(request):
    return render(request,"ToolsServices/SpecialLinks.html")

def SpecialLinkPage(request, linkId):
    # Get the data corresponding to the link from db.

    data = {
        'linkName' : 'File 0',
        'linkId' : linkId,
    }

    return render(request,'ToolsServices/SpecialLinkPages/SpecialLinkPage.html',context = data)