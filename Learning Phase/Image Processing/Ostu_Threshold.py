import cv2 

img = cv2.imread('1.jpg') 

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# applying Ostu thresholding 
ret, thr = cv2.threshold(gray_img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)	 
 
cv2.imshow('Otsu Threshold', thr)		 
	
cv2.waitKey(0)
cv2.destroyAllWindows()	 
