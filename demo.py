import cv2
import numpy as np
import __data__ as data

img = cv2.imread('test.jpg')

#convert cvt
HSVimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#HSVtestimg = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
cv2.imshow('Org', img)
cv2.imshow('HSV', HSVimg)

#cv2.imshow('HSVtest', HSVtestimg)
cv2.imwrite('testHSV.jpg', HSVimg)

imgThresholded = cv2.inRange(HSVimg, (data.iMinH, data.iMinS, data.iMinV), (data.iMaxH, data.iMaxS, data.iMaxV))
cv2.imshow('recOriginal', imgThresholded)
#open operation
ele = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
imgThresholded = cv2.morphologyEx(imgThresholded, cv2.MORPH_CLOSE, ele)
cv2.imshow('recOpen', imgThresholded)
#close operation
imgThresholded = cv2.morphologyEx(imgThresholded, cv2.MORPH_CLOSE, ele)

cv2.imshow('recClose', imgThresholded)

cv2.waitKey(0)

cv2.destroyAllWindows()