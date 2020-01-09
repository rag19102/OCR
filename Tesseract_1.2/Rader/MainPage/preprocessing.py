import cv2
import os
import easygui
import numpy as np
import pytesseract as pt
from matplotlib import pyplot as plt
class Preprocessing:
    def ConvertImageToGray(imagePath):
        grayImage = cv2.cvtColor(imagePath, cv2.COLOR_BGR2GRAY)
        grayImage = cv2.bitwise_not(grayImage)
        thresh = cv2.threshold(grayImage, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        return thresh

    def ImageRotation(image):
        #get the coordinates of an image
        co_Ordinates = np.column_stack(np.where(image > 0))
        #get the angle  of the image
        angle = cv2.minAreaRect(co_Ordinates)[-1]
        if(angle < -45):
            angle=-(90+angle)
        else:
            angle = -angle

        #Now we got the angle of the image
        #rotate the image to correct position
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated

    def ApplyGaussianBlur(img):
        th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        return th3

    def EdgeDetection(img):
        width = 400
        height =400
        dim = (width, height)
        cv2.resize(img,(800,800))
        return cv2.canny(img,30
        ,50)

    def ImageToBoxes(imgurl):
        img = cv2.imread(imgurl)    
        #Pytesseract image to boxes
        BoxedImage = pt.image_to_boxes(img)
        h, w, _ = img.shape

        for b in BoxedImage.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

        path = cv2.imwrite("media/"+imgurl+".jpg",img)
        return path
        