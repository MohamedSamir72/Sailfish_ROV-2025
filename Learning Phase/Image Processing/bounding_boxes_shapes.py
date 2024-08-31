import cv2
import numpy as np

img = cv2.imread('8.jpg')

img = cv2.resize(img, (720, 480))
copy_img = img.copy()
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thr = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv2.drawContours(copy_img, contours, -1, (0, 255, 0), 2)

# Draw bounding boxes around each detected contour
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


# Display the combined image
# cv2.imshow('thresholod', thr)
cv2.imshow('Final Image with bounding boxes', img)
cv2.imshow('Final Image with contours', copy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()