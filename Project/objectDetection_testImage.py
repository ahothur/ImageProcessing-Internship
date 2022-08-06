# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:34:02 2022

@author: ahoth
"""

import objectDetection as o
import cv2

def main():
    
    base_path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Project/Images/img'
    weights_path = "C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Project/yolov3-spp.weights"
    cfg_path = "C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Project/yolov3-spp.cfg"
    
    
    for i in range(1,8):
        # Load image for detection
        path = base_path + str(i) + ".jpg"
        image = cv2.imread(path)
        
        # Display Image
        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        img = o.usePreTrainedModel(image, weights_path, cfg_path)
        
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    
main()