from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):

    return render(request, 'index.html' )

def Upload(request):
    url =""
    if(request.method=='POST'):
        upload_file =request.FILES['document']
        storefile = FileSystemStorage()
        url = storefile.save(upload_file.name, upload_file)
        url = 'media/'+ url
    return render(request, 'index.html', {'url':url})

def Dashboard(request):
    if(request=='POST'):
        Upload_File = request.FILES['document']
        storefile = FileSystemStorage()
        return render(request, 'Dashboard.html')
    else:
        return render(request, 'Dashboard.html')
    

def Result(request):
    return render(request, 'Result.html')