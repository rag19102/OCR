from django.shortcuts import render
from django.http import HttpResponse 
import easygui
import pytesseract
import cv2
from pdf2image import convert_from_path

data = ''
# Create your views here.
def home(request):
    return render(request, 'Dashboard.html')

def UploadFile(request):
    imageFilePath = easygui.fileopenbox()
    actualImage = cv2.imread(imageFilePath)
    grayImage = cv2.cvtColor(actualImage, cv2.COLOR_BGR2GRAY)
 

    imageData = '3-2memo.jpeg'
    imageText = pytesseract.image_to_string(grayImage)
    data = imageFilePath

    return render(request, 'Dashboard.html',{'data':imageFilePath,'data1':imageText, 'imageData':imageData})

# def TesseractOcrButtonClicked(request):
#     imageText = pytesseract.image_to_string('G:\\3-2 memo.jpeg')
#     return HttpResponse(request, 'Dashboard.html',{'data1':imageText})


# def PDF_OCR():
