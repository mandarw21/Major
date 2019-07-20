# -*- coding: utf-8 -*-
"""
Created on Thu Mar 07 15:04:53 2019

@author: Trevor
"""
import time
import cv2
import datetime
import os
import multiprocessing
from mongoDB_SendString import UploadImage


def detect_faces():

    face_cascade = cv2.CascadeClassifier('/home/krypton/Documents/haarcascades/haarcascade_frontalface_default.xml')
    
    
    cap = cv2.VideoCapture(0)
    path ='/home/krypton/Documents/Image'
    imgCtr=0
    
    
    
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
        for (x,y,w,h) in faces:
            
    #=============== Image Naming ===================================
    
            sysTime = datetime.datetime.now()
            deviceTime=sysTime.strftime("%d_%m_%Y_%H_%M_%S_%f")
            imageName = "Cam1_"+deviceTime+".png"
            
    #=============== Image Naming block complete ====================
            
            cv2.rectangle(img,(x,y),(x+w,y+h),(57,255,20),2)
            #roi_gray = gray[y:y+h, x:x+w]
            #roi_color = img[y:y+h, x:x+w]
            
            sub_face = img[y:y+h, x:x+w]
            imgCtr+=1
            
            if(imgCtr==5):
                cv2.imwrite(os.path.join(path , imageName), sub_face)
                imgCtr=0    
                
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
def upload_images():
       
    obj = UploadImage()
    starttime=time.time()
    try: 
        while True:    
            obj.upload()
            time.sleep(60.0 -((time.time() - starttime) % 60.0))
    except KeyboardInterrupt:
        pass
                    

if __name__ == "__main__":
    
    p1 = multiprocessing.Process(target=detect_faces)
    p2 = multiprocessing.Process(target=upload_images)
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
