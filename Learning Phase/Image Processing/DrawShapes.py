import numpy as np
import cv2

# Define colors and text properties 
black_color =   (0, 0, 0)
blue_color =    (255, 0, 0)
green_color =   (0, 255, 0)
red_color =     (0, 0, 255)
font_type = cv2.FONT_HERSHEY_SIMPLEX
thickness = 2
font_scale = 0.5

# Create the main components of background
image = np.ones((720, 680, 3), dtype=np.uint8) * 255
cv2.putText(image, "Tomb Area", (260, 30), font_type, 1, black_color, thickness)
cv2.rectangle(image, (40, 40), (640, 660), black_color, thickness)

cv2.putText(image, "Pharaoh Treasure", (50, 680), font_type, font_scale, blue_color, thickness)
cv2.putText(image, "Pharaoh Coffin", (270, 680), font_type, font_scale, green_color, thickness)
cv2.putText(image, "Papyrus paper roll", (480, 680), font_type, font_scale, red_color, thickness)

# Draw different shapes
x1 = 70
y1 = 90
cv2.rectangle(image, (x1-20, y1-20), (x1+20, y1+20), blue_color, -1)
cv2.putText(image, "1", (x1-20, y1-25), font_type, font_scale, blue_color, 1)

x2 = 455
y2 = 300
cv2.rectangle(image, (x2-20, y2-20), (x2+20, y2+20), blue_color, -1)
cv2.putText(image, "2", (x2-20, y2-25), font_type, font_scale, blue_color, 1)

x3 = 210
y3 = 130
cv2.rectangle(image, (x3-20, y3-20), (x3+20, y3+20), green_color, -1)
cv2.putText(image, "1", (x3-20, y3-25), font_type, font_scale, green_color, 1)

x4 = 130
y4 = 600
cv2.rectangle(image, (x4-20, y4-20), (x4+20, y4+20), green_color, -1)
cv2.putText(image, "2", (x4-20, y4-25), font_type, font_scale, green_color, 1)

x5 = 220
y5 = 250
cv2.circle(image, (x5, y5), 20, (0,0,255), -1)
cv2.putText(image, "1", (x5-20, y5-25), font_type, font_scale, red_color, 1)

x6 = 500
y6 = 600
cv2.circle(image, (x6, y6), 20, (0,0,255), -1)
cv2.putText(image, "2", (x6-20, y6-25), font_type, font_scale, red_color, 1)

x7 = 100
y7 = 400
cv2.circle(image, (x7, y7), 20, (0,0,255), -1)
cv2.putText(image, "3", (x7-20, y7-25), font_type, font_scale, red_color, 1)


cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
