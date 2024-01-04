'''
First you have to download the openCV built-in, trained HaarCascade model (XML file)
https://github.com/opencv/opencv/tree/master/data/haarcascades

you can also download the different pre-trained models to detect different objects from 
the above same link
'''

import cv2

# Adding face detection haar cascade model
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread('lina.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Finding faces in an image using face cascade
# 1.1 is the scale factor, low scale value means better results but will require more computational power
# 4 is the minimun neabours, lower minimun neabour means much more detection but might have false detection as well
face = face_cascade.detectMultiScale(img_gray, 1.1, 4)
#print(face)


for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2q)

cv2.imshow('output', img)
cv2.waitKey(0)


