from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import pytesseract
import os
import requests
 
def button(request):
    text = pytesseract.image_to_string('matcherator_help_clear.png')
    return HttpResponse(text)
def myView(request):
    return render(request,'home.html')
    # text = pytesseract.image_to_string('P-AadhaarCard.jpg')
    # return HttpResponse(text)