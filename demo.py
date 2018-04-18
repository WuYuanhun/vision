# Create By Wu_Yuanhun (Liu Cetian) 
# github @ WuYuanhun
# mail @ wu_yuanhun@qq.com
# From FRC team5308
# Demo

import cv2
import numpy as np
import __data__ as data

cap = cv2.VideoCapture(2)

ret, img = cap.read()

#save original image
cv2.imwrite('source.jpg', img)

#convert color space to HSV 
HSVimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('source', img)
cv2.imshow('HSV', HSVimg)

# find color in range
imgThresholded = cv2.inRange(HSVimg, (data.iMinH, data.iMinS, data.iMinV), (data.iMaxH, data.iMaxS, data.iMaxV))
cv2.imshow('recOrg', imgThresholded)

ele = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

#open operation
imgThresholded = cv2.morphologyEx(imgThresholded, cv2.MORPH_CLOSE, ele)

#close operation
imgThresholded = cv2.morphologyEx(imgThresholded, cv2.MORPH_CLOSE, ele)

#print standard rev
cv2.imshow('OutColor', imgThresholded)

cv2.imwrite('sourceREC.jpg', imgThresholded)


cv2.waitKey(0)

# release camera and quit windows
cap.release()
cv2.destroyAllWindows()