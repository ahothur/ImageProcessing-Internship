# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 08:57:50 2022

@author: ahoth
"""

import cv2
import numpy as np
import objectDetection as o

fgbg = cv2.createBackgroundSubtractorMOG2()

base_path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Project/Videos/'
weights_path = "C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Project/yolov3-spp.weights"
cfg_path = "C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Project/yolov3-spp.cfg"

path = base_path + 'vtest.avi'

vid = cv2.VideoCapture(path)

w, h = int(vid.get(3)), int(vid.get(4))

out1 = cv2.VideoWriter(base_path + 'sample1.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 17, (w, h))
out2 = cv2.VideoWriter(base_path + 'vtest_out2.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 17, (w, h))

while(True):
    #read from video
    ret, frame = vid.read() 
    if frame is None:
        break
    
    # Get mask
    fgmask = fgbg.apply(frame)
      
    # Creating new mask 
    # Converting mask to BGR image
    new_mask = np.dstack((fgmask,fgmask,fgmask))
    
    
    # Mask foreground objects
    new_frame = cv2.bitwise_or(new_mask, frame)
    
    #cv2.imshow('Frame', frame)
    cv2.imshow('FG mask', new_mask)
    cv2.imshow('Frame', new_frame)
    
    detected1 = o.usePreTrainedModel(frame, weights_path, cfg_path)
    detected2 = o.usePreTrainedModel(frame, weights_path, cfg_path)
    #detected2= o.usePreTrainedModel(new_frame, weights_path, cfg_path, frame)
    
    #Write the frame to video
    out1.write(detected1)
    out2.write(detected2)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
vid.release()
out1.release()
out2.release()
cv2.destroyAllWindows()





