from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from . import preprocessing
# Create your views here.
global filename 
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
    is_private = request.POST.get('is_private', False)
    url =""
    if(request.method=='POST' and 'Upload' in request.POST):
        upload_file = request.FILES['document']
        storefile = FileSystemStorage()
        filename = storefile.save(upload_file.name, upload_file)
        filepath = 'media/' + filename
        return render(request, 'Dashboard.html',{'data':"File Uploaded Sucessfully", 'url' : filename, 'path': filepath})
    elif(request.method=='POST' and 'GetText' in request.POST):
        imageName = request.POST.get("imagename")
        url = 'media/'+ imageName
        text = preprocessing.pt.image_to_string(url)

        BoxedImage = preprocessing.Preprocessing.ImageToBoxes(url)
        print(BoxedImage)
        # storefile = FileSystemStorage()
        # url = storefile.save(url+'Box', BoxedImage) 
        return render(request, 'Result.html',{'data':"media/media/" + imageName +".jpg",'text':text}) 
    else:
        return render(request, 'Dashboard.html')
    

def Result(request):
    return render(request, 'Result.html')
