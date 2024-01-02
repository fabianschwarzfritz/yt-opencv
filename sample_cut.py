#!/usr/bin/env python3

import cv2
from pathlib import Path

filename = str(Path.home()) + "/Downloads/asdf.jpeg"

img = cv2.imread(filename)

################### ADDITION

# img = img[int(img.shape[0]/2):img.shape[0]]
height, width, channels = img.shape
cropped = img[int(height/2):height, 0:width]

#################### END ADDITION

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
(people, _) = hog.detectMultiScale(cropped)

for (x, y, w, h) in people:
    cv2.rectangle(cropped, (x, y), (x+w, y+w), (0, 255, 0), 2)

cv2.imshow("Detected people", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
