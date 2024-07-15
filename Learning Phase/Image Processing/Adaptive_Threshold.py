import cv2 
import numpy as np 

img = cv2.imread('4.jpg') 

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Adaptive threshold
mean_thr = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 191, 3) 
gaussian_thr = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 191, 3) 

cv2.imshow("Original Image", img)
cv2.imshow('Adaptive Mean', mean_thr) 
cv2.imshow('Adaptive Gaussian', gaussian_thr) 

cv2.waitKey(0)
cv2.destroyAllWindows() 
