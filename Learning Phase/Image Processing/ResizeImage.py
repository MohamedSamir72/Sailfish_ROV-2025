import cv2

# Read an image
img1 = cv2.imread("1.jpg")

# Show the shape of the orignal image 
height, width, channel = img1.shape
print(f"Height: {height}\nWidth: {width}")

# Resize an image in two different ways
fx=0.3
fy=0.3
img2 = cv2.resize(img1, (480, 360))
img3 = cv2.resize(img1, None, fx=fx, fy=fy, )

# Show the shape of the resized image 
height, width, channel = img3.shape
print(f"Height: {height}\nWidth: {width}")

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Image 3", img3)

# Check if user clicked q to destroy windows or not
while True:
    key = cv2.waitKey(0)
    if key == ord('q'):
        print("Done")
        cv2.destroyAllWindows()
        break
