# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:07:54 2019

@author: Heisenberg
"""
import urllib
import cv2
import numpy as np
import sys
# Get user supplied values
imagePath = sys.argv[0]



url='http://192.168.43.1:8080/photo.jpg'
imgResp=urllib.request.urlopen(url)
imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
img=cv2.imdecode(imgNp,-1)
#cv2.imshow('t',img)




# Create the haar cascade
new_path = 'C://Users//Heisenberg//Anaconda3//Library//etc//haarcascades//haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(new_path)
eye_cascade = cv2.CascadeClassifier('C://Users//Heisenberg//Anaconda3//Library//etc//haarcascades//haarcascade_eye.xml')

# Read the image
#image = cv2.imread(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.31,
    minNeighbors=3,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print(f"Found {len(faces)} faces!")

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
