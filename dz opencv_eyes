import cv2
import numpy as np

video = cv2.VideoCapture(0)

eyes = cv2.CascadeClassifier('opencv_eyes.xml')

while True:
    success, img = video.read()

    results = eyes.detectMultiScale(img, scaleFactor=1.1, minNeighbors=30)

    if list(results):
        x, y, w, h = results[0]
        img2 = img[y:y+h, x-x//2:x+w+x//2]
        img2 = cv2.GaussianBlur(img2, (51, 51), 15)
        img[y:y+h, x-x//2:x+w+x//2] = img2

        cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
