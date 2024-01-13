from django.shortcuts import render, HttpResponse
import base64
import cv2
import pytesseract
import os

def index(request):
    return render(request, 'index.html')

def ocr(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data', '')
        image_data = image_data.replace('data:image/jpeg;base64,', '').replace('data:image/png;base64,', '')
        image_data = image_data.encode()
        with open('uploaded_image.jpg', 'wb') as f:
            f.write(base64.b64decode(image_data))

        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

        img = cv2.imread('uploaded_image.jpg')
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        text = pytesseract.image_to_string(gray_img)
        os.remove('uploaded_image.jpg')

        return render(request, 'index.html', {'text': text})

    return HttpResponse("Error")
