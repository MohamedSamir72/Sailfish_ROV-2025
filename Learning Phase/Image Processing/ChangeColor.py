import cv2

# Read an original image
img = cv2.imread("3.jpg")

# Handle the image
height, width, _ = img.shape
# print(height)
# print(width)
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# 1st way to convert the color scale of an image
rgb_img = cv2.imread("3.jpg", cv2.IMREAD_COLOR)
gray_img = cv2.imread("3.jpg", cv2.IMREAD_GRAYSCALE)

# 2nd way to convert the color scale of an image
gray_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Show all results
cv2.imshow("Image", img)
cv2.imshow("RGB Image", rgb_img)
cv2.imshow("Gray Image", gray_img)
cv2.imshow("Gray Image 2", gray_img2)
cv2.imshow("HSV Image", hsv_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
