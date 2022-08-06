# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 10:18:42 2022

@author: ahoth
"""

import cv2
import objectDetection as o

def main():
    base_path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Project/Videos/'
    weights_path = "C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Project/yolov3-spp.weights"
    cfg_path = "C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Project/yolov3-spp.cfg"
    
    
    vid = cv2.VideoCapture(base_path + "vid2.mp4")
    
    if (vid.isOpened() == False):
        print("Error opening video")
        return
    
    w, h = int(vid.get(3)), int(vid.get(4))
    
    out = cv2.VideoWriter(base_path + 'sample.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 17, (w, h))
    
    while(True):
        #read from camera
        ret, frame = vid.read() #ret - isSuccessful? frame - image of frame
        
        # Video is over
        if frame is None:
            break
      
        # Perform object detection on the frame
        #cv2.imshow('frame', im)
        detected_objects_img = o.usePreTrainedModel(frame, weights_path, cfg_path)
        
        #Write the frame to video
        out.write(detected_objects_img)
        
        """
        #cv2.imshow('video', detected_objects_img)
        
        # Displays image for 1 ms 
        # if 'q' key is pressed, stop reading from camera
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        """
    
    vid.release()
    out.release()
    cv2.destroyAllWindows()
    
    
main()