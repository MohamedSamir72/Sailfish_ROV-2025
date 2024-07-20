import numpy as np
import cv2

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x-20, y-20), (x+20, y+20), (255,0,0), -1)

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (0,255,0), -1)

name_window = "Image"

# A blank image
img = np.ones((480, 480, 3), dtype=np.uint8) * 255

# Creating a named window
cv2.namedWindow(name_window)

# Creating a callback function
cv2.setMouseCallback(name_window, mouse_event)

while True:
    cv2.imshow(name_window,img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
cv2.destroyAllWindows()