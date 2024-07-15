import numpy as np
import cv2

img1 = cv2.imread("6.png")
img2 = cv2.imread("5.png")

# concatenate two original images Horizontally 
original_img = np.concatenate((img1, img2), axis=1) 

dest_and = cv2.bitwise_and(img1, img2, mask=None)
dest_or = cv2.bitwise_or(img1, img2, mask=None)
dest_xor = cv2.bitwise_xor(img1, img2, mask=None)

dest_not1 = cv2.bitwise_not(img1, mask=None)
dest_not2 = cv2.bitwise_not(img2, mask=None)

# concatenate two images Horizontally 
dest_not = np.concatenate((dest_not1, dest_not2), axis=1) 

# Show an original image
cv2.imshow("image", original_img)

# Show outputs
cv2.imshow("Bitwise and", dest_and)
cv2.imshow("Bitwise Or", dest_or)
cv2.imshow("Bitwise xor", dest_xor)
cv2.imshow("Bitwise not", dest_not)

cv2.waitKey(0)
cv2.destroyAllWindows()

