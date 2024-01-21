from django.shortcuts import render

# Create your views here.
def FileUpload(request):
    return render(request,"FileTransfer/FileUpload.html")