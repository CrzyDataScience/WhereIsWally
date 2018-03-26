# Import OpenCV
import numpy as np
import cv2
import os
import sys

os.chdir("D:\Projects\CrazyDataScience\WhereIsWally")

# Set our cascade classifier we created earlier
# CASCADE_FILE = './classifier/haarcascade_frontalface_default.xml'
CASCADE_FILE = './classifier/cascade.xml'


# Load our cascade file
cascade = cv2.CascadeClassifier(CASCADE_FILE)


cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.105, 40)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()