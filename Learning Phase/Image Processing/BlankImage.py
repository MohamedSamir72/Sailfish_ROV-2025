import numpy as np
import cv2

# A blank image with black background
img1 = np.zeros((360, 480), dtype=np.uint8)

# A blank image with white background
img2 = np.ones((640, 720), dtype=np.uint8)
img2 *= 255

# A blank image with colored background
height = 360
width = 480
color = [255, 0, 0]

img3 = np.zeros((height, width, 3), dtype=np.uint8)
# Change the background color
for x in range(width):
    for y in range(height):
        img3[y, x] = color

# Show all results
cv2.imshow("img 1", img1)
cv2.imshow("img 2", img2)
cv2.imshow("img 3", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
