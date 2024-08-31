import cv2
import numpy as np

img = cv2.imread('7.png')

img = cv2.resize(img, (480, 360))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thr = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

# Define the kernel (structuring element)
kernel = np.ones((3,3), np.uint8)

# Apply erosion
erosion = cv2.erode(thr, kernel, iterations = 1)
# Apply dilation
dilation = cv2.dilate(thr, kernel, iterations = 1)
# Apply opening
opening = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel)
# Apply closing
closing = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel)




# Stack images horizontally and vertically to form a 2x2 grid
top_row = np.hstack((erosion, dilation))       
bottom_row = np.hstack((opening, closing))  

# Combine the two rows vertically
result = np.vstack((top_row, bottom_row))

# Optionally, add labels to each section of the result image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(result, 'Threshold', (30, 50), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(result, 'Erosion', (480 + 30, 50), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(result, 'Dilation', (50, 360 + 50), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(result, 'Opening', (480 + 50, 360 + 50), font, 1, (0, 0, 0), 1, cv2.LINE_AA)

cv2.imshow('thresholod', thr)
# Display the combined image
cv2.imshow('Morphological Transformations (2x2 Grid)', result)
cv2.waitKey(0)
cv2.destroyAllWindows()