import numpy as np
import cv2

name_window = "Image"
points = []

def mouse_event(event, x, y, flags, param):
    global points
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, (0,0,255), -1)
        print(x, y)

        if len(points) == 0 or not points[-1]:  # Start a new sublist if points is empty or the last sublist is empty
            points.append([(x, y)])
        else:
            cv2.line(img, points[-1][-1], (x, y), (0,255,0), 1, cv2.LINE_AA)
            points[-1].append((x, y))

        print(points)

    if event == cv2.EVENT_RBUTTONDOWN:
        # Start a new sublist for the new set of points
        points.append([])  
        print(points)


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
        points = [sublist for sublist in points if sublist]  # Remove empty sublists
        print(points)
        break
    
cv2.destroyAllWindows()
