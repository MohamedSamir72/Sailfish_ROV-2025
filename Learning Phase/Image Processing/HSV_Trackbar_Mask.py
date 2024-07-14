import cv2
import numpy as np

def nothing(x):
    pass

name_window = "RGB Color Trackbar"

cv2.namedWindow(name_window)

# create trackbars for color change
cv2.createTrackbar('HMin', name_window, 0, 179, nothing)  # Hue is from 0-179 for Opencv
cv2.createTrackbar('SMin', name_window, 0, 255, nothing)
cv2.createTrackbar('VMin', name_window, 0, 255, nothing)
cv2.createTrackbar('HMax', name_window, 0, 179, nothing)
cv2.createTrackbar('SMax', name_window, 0, 255, nothing)
cv2.createTrackbar('VMax', name_window, 0, 255, nothing)

# Set default value for MAX HSV trackbars
cv2.setTrackbarPos('HMax', name_window, 179)
cv2.setTrackbarPos('SMax', name_window, 255)
cv2.setTrackbarPos('VMax', name_window, 255)

# Load an image
image_path = '3.jpg'
image = cv2.imread(image_path)
image = cv2.resize(image, (640, 480))
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

while(1):
    # get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', name_window)
    sMin = cv2.getTrackbarPos('SMin', name_window)
    vMin = cv2.getTrackbarPos('VMin', name_window)
    hMax = cv2.getTrackbarPos('HMax', name_window)
    sMax = cv2.getTrackbarPos('SMax', name_window)
    vMax = cv2.getTrackbarPos('VMax', name_window)

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Create HSV Image and threshold into a range.
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display result image
    cv2.imshow(name_window, result)
    cv2.imshow('mask', mask)

    # Wait for ESC key to stop
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()

