# 12-20-2021
# Funtion to display what webcam sees

import cv2


# Playing capture

# Opening camera

def openWebcam():
    capture = cv2.VideoCapture(0) #opens camera 0
    time = 1
    
    while(True):
        #read from camera
        r, im = capture.read() #r - isSuccessful? im - image of frame
        cv2.imshow('frame', im)
        
        # Displays image for 1 ms 
        # if 'q' key is pressed, stop reading from camera
        if cv2.waitKey(time) & 0xFF == ord('q'):
            break
            
    capture.release()
    cv2.destroyAllWindows()
    
openWebcam()
    
