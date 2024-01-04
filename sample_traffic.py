#!/usr/bin/env python3

import cv2
from pathlib import Path
import time

filename = str(Path.home()) + "/Downloads/traffic/traffic2.mp4"
classifier = str(Path.home()) + "/Downloads/traffic/cars3.xml"

cap = cv2.VideoCapture(filename)
car_classifier = cv2.CascadeClassifier(classifier)

while True:
    ret, img = cap.read()
#    height, width, _ = img.shape
#    start_height = int(height/3)
#    end_height = int(height/6 * 5)
#    start_width = int(width/4 * 1)
#    end_width = int(width/4 * 3)
#    cropped = img[start_height:end_height, start_width: end_width]
    cropped = img

    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 5)
    cars = car_classifier.detectMultiScale(blur, 1.1, 1)
    for (x, y, w, h) in cars:
        cv2.rectangle(cropped, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('video', img)

    escape = 27
    if cv2.waitKey(33) == escape:
        break

cv2.destroyAllWindows()

