#!/usr/env/bin python3

import cv2
from pathlib import Path

filename = str(Path.home()) + "/Downloads/asdf.jpeg"

img = cv2.imread(filename)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
(people, _) = hog.detectMultiScale(img)

for (x, y, w, h) in people:
    cv2.rectangle(img, (x, y), (x+w, y+w), (0, 255, 0), 2)

cv2.imshow("Detected people", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
