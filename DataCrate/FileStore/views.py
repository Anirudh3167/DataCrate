from django.shortcuts import render

# Create your views here.
def Home(request):
    data = {
        'files' : [
            {'filename' : 'file 1', 'publishedDate':'10-01-2023', 'fileType' : 'pdf'},
            {'filename' : 'file 1', 'publishedDate':'10-01-2023', 'fileType' : 'xml'},
            {'filename' : 'file 1', 'publishedDate':'10-01-2023', 'fileType' : 'docx'},
        ]
    }
    return render(request,"FileStore/FileStoreHome.html", context = data)