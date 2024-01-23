from django.shortcuts import render

# Create your views here.
def FileShare(request):
    return render(request,"FileTransfer/FileShare.html")