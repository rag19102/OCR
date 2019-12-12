from django.shortcuts import render
from django.http import HttpResponse 
import easygui
import pytesseract

data = ''
# Create your views here.
def home(request):
    return render(request, 'Dashboard.html')

def UploadFile(request):
    imageFilePath = easygui.fileopenbox()
    imageText = pytesseract.image_to_string(imageFilePath)
    data = imageFilePath

    return render(request, 'Dashboard.html',{'data':imageFilePath,'data1':imageText})

def TesseractOcrButtonClicked(request):
    imageText = pytesseract.image_to_string('G:\\3-2 memo.jpeg')
    return HttpResponse(request, 'Dashboard.html',{'data1':imageText})