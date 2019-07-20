import cv2
import numpy as np
import sys
# Get user supplied values
imagePath = sys.argv[0]


# Create the haar cascade
new_path = 'C://Users//Heisenberg//Anaconda3//Library//etc//haarcascades//haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(new_path)

# Read the image
image = cv2.imread('D://Pics//New folder//Images//download2.jfif')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
