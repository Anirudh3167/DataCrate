import os
from django.shortcuts import render
from django.http import JsonResponse, FileResponse
import json

# Create your views here.
def FileShare(request):
    return render(request,"FileTransfer/FileShare.html")

def get_next_folder_count():
    # Get a list of all directories in './Files'
    directories = [d for d in os.listdir('./Files') if os.path.isdir(os.path.join('./Files', d))]
    
    if not directories:
        return 1  # If no directories exist, start with 1
    else:
        # Find the highest number in the existing directories
        folder_counts = [int(d.split('_')[-1]) for d in directories]
        return max(folder_counts) + 1
    
def FileUpload(request):
    if (request.method == 'POST'):
        # print(json.load(request))
        if (request.FILES):
            files = request.FILES.getlist('fileInput')
            print(f'Recieved Files of total count:{len(files)}')
            next_folder_count = get_next_folder_count()
            save_path = f'./Files/{next_folder_count}' # get the folders count
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            for file in files:
                with open(os.path.join(save_path, file.name), 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
        else:
            print('It is not working')
        data = {
            "recieved" : True,
            "code" : next_folder_count,
        }
        return JsonResponse(data)
    return render(request,"FileTransfer/FileShare.html")

def FileDownload(request,id):
    # path = 'C://Users/Anirudh/Desktop/Printout'
    path = f'./Files/{id}/'
    if (request.method == 'GET'):
        # Requesting the metadata of files for selective download
        if request.GET.get('request-type') == 'MetaDataRequest':
            # For the files link
            filenames = os.listdir(path)

            meta_data = {
                'files' : [],
                'Code' : {}
            }
            for idx in range(len(filenames)):
                meta_data['files'].append({'filename':filenames[idx], 'index' : idx})

            # For the Editor links
            if (request.GET.get('code') == 'editor'):
                meta_data = {
                    'files' : [],
                    'Code' : {
                        "content" : "Hello World",
                        "date" : "12-03-2024",
                    }
                }
            return JsonResponse(meta_data)
        else:   # Requesting for a single file download.
            # request.GET.get('request-type') == 'FileDownloadRequest'
            filenames = os.listdir(path)

            idx = int(request.GET.get('index'))
            print(filenames[idx])
            response = FileResponse(open(path + f'/{filenames[idx]}','rb'))
            # response['Access-Control-Expose-Headers'] = 'Content-Disposition'
            response["Content-Disposition"] = f"attachment; filename={filenames[idx]}"
            return response