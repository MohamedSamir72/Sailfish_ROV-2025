import numpy as np 
import cv2 

# empty function called when any trackbar moves 
def emptyFunction(x): 
    pass

def main(): 
    # blackwindow having 3 color channels 
    image = np.zeros((512, 512, 3), np.uint8) 
    name_window = "RGB Color Trackbar"
    
    # window name 
    cv2.namedWindow(name_window) 
    
    # there trackbars which have the name of trackbars min and max value 
    cv2.createTrackbar('Blue', name_window, 0, 255, emptyFunction) 
    cv2.createTrackbar('Green', name_window, 0, 255, emptyFunction) 
    cv2.createTrackbar('Red', name_window, 0, 255, emptyFunction) 
    

    while(True): 
        cv2.imshow(name_window, image) 
        
        if cv2.waitKey(1) == 27: 
            break
        
        # values of blue, green, red 
        blue = cv2.getTrackbarPos('Blue', name_window) 
        green = cv2.getTrackbarPos('Green', name_window) 
        red = cv2.getTrackbarPos('Red', name_window) 
        
        # merge all three color channels and make the image composites image from rgb 
        image[:] = [blue, green, red] 
        print(blue, green, red) 
        
    cv2.destroyAllWindows() 

		 
if __name__=="__main__": 
    main() 
