from django.shortcuts import render
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
    
