import numpy as np
import cv2

img = cv2.imread("2.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple Thresholding
_, thr1 = cv2.threshold(gray_img, 172, 255, cv2.THRESH_BINARY)
_, thr2 = cv2.threshold(gray_img, 172, 255, cv2.THRESH_BINARY_INV)
_, thr3 = cv2.threshold(gray_img, 60, 255, cv2.THRESH_TOZERO)
_, thr4 = cv2.threshold(gray_img, 60, 255, cv2.THRESH_TOZERO_INV)
_, thr5 = cv2.threshold(gray_img, 180, 255, cv2.THRESH_TRUNC)

cv2.imshow("Image", img)
cv2.imshow("Thresh 1", thr1)
cv2.imshow("Thresh 2", thr2)
cv2.imshow("Thresh 3", thr3)
cv2.imshow("Thresh 4", thr4)
cv2.imshow("Thresh 5", thr5)

cv2.waitKey(0)
cv2.destroyAllWindows()