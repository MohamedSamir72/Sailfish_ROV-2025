import numpy as np 
import cv2 

# empty function called when any trackbar moves 
def emptyFunction(pos): 
    pass

def main(): 
    # blackwindow having 3 color channels 
    image = np.zeros((512, 512, 3), np.uint8) 
    windowName = "Open CV Color Trackbar"
    
    # window name 
    cv2.namedWindow(windowName) 
    
    # there trackbars which have the name of trackbars min and max value 
    cv2.createTrackbar('Blue', windowName, 0, 255, emptyFunction) 
    cv2.createTrackbar('Green', windowName, 0, 255, emptyFunction) 
    cv2.createTrackbar('Red', windowName, 0, 255, emptyFunction) 
    

    while(True): 
        cv2.imshow(windowName, image) 
        
        if cv2.waitKey(1) == 27: 
            break
        
        # values of blue, green, red 
        blue = cv2.getTrackbarPos('Blue', windowName) 
        green = cv2.getTrackbarPos('Green', windowName) 
        red = cv2.getTrackbarPos('Red', windowName) 
        
        # merge all three color channels and make the image composites image from rgb 
        image[:] = [blue, green, red] 
        print(blue, green, red) 
        
    cv2.destroyAllWindows() 

		 
if __name__=="__main__": 
    main() 
