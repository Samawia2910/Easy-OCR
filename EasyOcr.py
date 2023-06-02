# Python program to explain
# cv2.polylines() method
import cv2
import numpy as np
# Reading an image in default
# mode
image = cv2.imread("chinese.jpg")

penta_points = np.array([[[50,150],[130,100],[190,150],[170,270],[90,250]]], np.int32)
polygon = cv2.polylines(image, [penta_points], True, (0,255,0), 5)
cv2.imshow("Polygon", polygon)
cv2.waitKey(0)
cv2.destroyAllWindows()
